# Import standard libraries for UI construction, REST API interaction, and temporal data handling
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- Page Configuration ---
# Configure the Streamlit application page parameters and centralized layout
st.set_page_config(
    page_title="Used Car Price Predictor",
    layout="centered"
)

# --- Aggressive Dark Theme & Full-Width CSS ---
# Inject custom CSS to enforce a deep charcoal aesthetic and normalize input field styling
st.markdown("""
    <style>
    /* Enforce Deep Charcoal Background */
    .stApp { background-color: #1e2129; color: #ffffff; }
    
    /* Global Text Styling */
    h1, h2, h3, p, label { color: #d1d1d1 !important; font-family: 'Inter', sans-serif; }
    
    /* Input Field Styling */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #2b2e3a !important; color: white !important; border-radius: 6px;
    }
    
    /* Force THE Button to span EVERYTHING */
    div.stButton > button:first-child {
        background-color: #6e6e6e; 
        color: white; 
        border-radius: 8px; 
        height: 3em; 
        width: 100%; 
        font-weight: bold; 
        font-size: 20px;
        text-transform: uppercase;
        border: none;
    }
    
    div.stButton > button:hover {
        background-color: #ff4b4b; 
        color: white;
    }

    /* Slider Styling */
    .stSlider > div > div > div > div { background: #ff4b4b; }
    
    /* Clean Divider */
    hr { border-top: 2px solid #3d4150 !important; }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
# Initialize the primary dashboard header and instructional narrative
st.title("Car Valuation Dashboard")
st.markdown("Enter the vehicle specifications below to generate a real-time market appraisal.")

# --- Input Parameters: Manufacturer and Model ---
# Construct the first row of features using a dual-column layout
r1_col1, r1_col2 = st.columns(2)
with r1_col1:
    make = st.text_input("Manufacturer", value="Ford")
with r1_col2:
    model_name = st.text_input("Model (e.g., Fiesta, Golf)", value="Fiesta")

# --- Input Parameters: Transmission and Production Year ---
# Define mechanical and temporal features for the second input row
r2_col1, r2_col2 = st.columns(2)
with r2_col1:
    transmission = st.selectbox("Transmission", ["Manual", "Automatic", "Semi-Auto"])
with r2_col2:
    year = st.number_input("Production Year", min_value=1990, max_value=2026, value=2020)

# --- Input Parameters: Fuel Type and Usage Metrics ---
# Capture engine technology and cumulative mileage data
r3_col1, r3_col2 = st.columns(2)
with r3_col1:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid", "Electric", "Other"])
with r3_col2:
    mileage = st.number_input("Current Mileage", min_value=0, value=30000, step=1000)

# --- Input Parameters: Efficiency and Displacement ---
# Collect performance-related features and visualize engine size displacement
r4_col1, r4_col2 = st.columns(2)
with r4_col1:
    mpg = st.number_input("Fuel Efficiency (MPG)", min_value=1.0, value=45.0)
with r4_col2:
    engine_size = st.slider("Engine Size (L)", 0.0, 6.0, 1.6, 0.1)

# --- Regional Context Selection ---
# Identify the target market region for localized valuation
country = st.selectbox("Market Region", ["UK", "USA"])

# --- Action Section ---
# Apply a visual break before executing the inference trigger
st.divider()

# --- Payload Construction and Backend Inference ---
# Execute the prediction logic by transmitting a serialized payload to the FastAPI service
if st.button("Get Valuation", use_container_width=True):
    # Normalize and wrap input data into a standardized request body
    payload = {
        "make": make,
        "model": model_name,
        "year": year,
        "mileage": mileage,
        "transmission": transmission,
        "fuelType": fuel_type,
        "country": country.lower(),
        "engineSize": engine_size,
        "mpg": mpg
    }
    
    try:
        # Communicate with the local inference server and handle temporal latency
        with st.spinner(f"Analyzing {country} Market Data..."):
            response = requests.post("http://localhost:8000/predict", json=payload)
            result = response.json()
            
            # Verify successful inference and render valuation metrics
            if result["status"] == "success":
                st.divider()
                st.subheader(f"Valuation Results ({country})")
                
                # Display dynamic currency conversions using 2026 market context
                m1, m2 = st.columns(2)
                m1.metric("Valuation (GBP)", f"£{result['predicted_valuation_gbp']:,}")
                m2.metric("Valuation (USD)", f"${result['predicted_valuation_usd']:,}")
                
                # Output market confidence metadata based on regional presence
                st.info(f"Market Confidence: {result['market_confidence']}")
            else:
                # Handle application-level errors returned by the service
                st.error(f"Error: {result['message']}")
                
    except Exception as e:
        # Output critical connection logs if the backend service is unreachable
        st.error("Connection Failed: Backend server not reachable.")