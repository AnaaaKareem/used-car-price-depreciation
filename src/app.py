# Import standard libraries for API construction, temporal logic, and model serialization
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import joblib
import pandas as pd
import os
import requests

# Setup relative directory paths for model artifact ingestion
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')

# Initialize the FastAPI application instance
app = FastAPI(title="Car Valuation Service")

# Initialize global variables for model artifacts and imputation metadata
model = None
model_features = None
mpg_med = 45.0
eng_med = 1.6

# Execute the model loading phase to pull the deployment bundle into memory
try:
    # Load the serialized deployment bundle using joblib
    bundle = joblib.load(MODEL_PATH)
    
    # Extract the fitted pipeline and metadata from the bundle
    model = bundle['pipeline']
    
    # Retrieve imputation constants and feature names from the metadata dictionary
    mpg_med = bundle.get('non_ev_mpg_median', 45.0)
    eng_med = bundle.get('non_ev_engine_median', 1.6)
    model_features = bundle.get('feature_columns', [])
    
    print(f"Successfully initialized model with {len(model_features)} features")
except Exception as e:
    # Output error log if the model loading phase fails
    print(f"Critical Error: Failed to load model bundle - {e}")

# Define a helper function to retrieve live market exchange rates
def get_live_exchange_rate():
    try:
        # Fetching latest currency exchange rates from a public API (USD base)
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        data = response.json()
        return data['rates']['GBP']
    except Exception as e:
        print(f"FX Error: Could not fetch live rates ({e}). Falling back to 0.78")
        return 0.78

# Define the Pydantic schema for incoming valuation requests to ensure data integrity
class CarRequest(BaseModel):
    make: str
    model: str
    year: int
    mileage: float
    transmission: str
    fuelType: str
    country: str

@app.post("/predict")
def predict_price(data: CarRequest):
    # Verify model initialization before proceeding to inference
    if model is None or not model_features:
        return {
            "status": "error",
            "message": "Model artifacts not found. Deployment aborted."
        }

    # Identify the current temporal context for dynamic age calculation
    current_year = datetime.now().year

    # --- Feature Engineering and Normalization ---
    # Construct the raw record dictionary with standardized naming and casing
    record = {
        'make': data.make.strip().title(),
        'model': data.model.strip().title(),
        'year': data.year,
        'mileage': data.mileage,
        'transmission': data.transmission.strip().title(),
        'fuelType': data.fuelType.strip().title(),
        'country': data.country.strip().lower(),
        'age': current_year - data.year,
        'is_ev': 1 if data.fuelType.lower() == 'electric' else 0
    }

    # --- Imputation ---
    # Apply ICE-based medians to Electric Vehicles to standardize the input space
    if record['is_ev'] == 1:
        record['mpg'] = mpg_med
        record['engineSize'] = eng_med
    else:
        # Assign standard fallback values for non-EV records if specific data is missing
        record['mpg'] = 45.0 
        record['engineSize'] = 1.6

    # Convert the processed record into a pandas dataframe for pipeline compatibility
    input_df = pd.DataFrame([record])

    # --- Manual Categorical Encoding ---
    # Align binary flags with the training set schema (Title Case alignment)
    input_df['country_uk'] = 1 if record['country'] == 'uk' else 0
    input_df['transmission_Automatic'] = 1 if record['transmission'] == 'Automatic' else 0
    input_df['transmission_Manual'] = 1 if record['transmission'] == 'Manual' else 0
    input_df['transmission_Semi-Auto'] = 1 if record['transmission'] == 'Semi-Auto' else 0
    
    # Expand fuel type flags to support hybrid and traditional combustion engines
    input_df['fuelType_Electric'] = 1 if record['fuelType'] == 'Electric' else 0
    input_df['fuelType_Petrol'] = 1 if record['fuelType'] == 'Petrol' else 0
    input_df['fuelType_Hybrid'] = 1 if record['fuelType'] == 'Hybrid' else 0
    input_df['fuelType_Diesel'] = 1 if record['fuelType'] == 'Diesel' else 0
    input_df['fuelType_Other'] = 1 if record['fuelType'] == 'Other' else 0

    # Reindex the dataframe to ensure feature order matches the training matrix exactly
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    # --- Inference and Dynamic Currency Conversion ---
    # Execute the prediction to retrieve valuation in USD
    prediction_usd = float(model.predict(input_df)[0])
    
    # Fetch the live exchange rate for the 2026 market context
    fx_rate = get_live_exchange_rate()
    prediction_gbp = prediction_usd * fx_rate

    # Return the finalized valuation response with deployment metadata
    return {
        "status": "success",
        "vehicle": f"{data.year} {record['make']} {record['model']}",
        "predicted_valuation_gbp": round(prediction_gbp, 2),
        "predicted_valuation_usd": round(prediction_usd, 2),
        "market_context": {
            "is_uk_market": bool(input_df['country_uk'][0]),
            "calculated_age": record['age'],
            "imputation_applied": bool(record['is_ev']),
            "exchange_rate_used": round(fx_rate, 2),
            "rate_source": "Live Market API" if fx_rate != 0.78 else "Static Fallback"
        },
        "system_info": {
            "timestamp": datetime.now().isoformat(),
            "model_version": "2.1.0-RF"
        }
    }