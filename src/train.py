# Import standard libraries for high-level data handling and model serialization
import pandas as pd
import numpy as np
import joblib
import os

# Import scikit-learn components for pipeline construction, validation, and hyperparameter tuning
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

# Import binary encoder to handle high-cardinality features using bit-representative columns
from category_encoders import BinaryEncoder

# Define relative directory paths for processed data ingestion and model storage
PROCESSED_DATA_DIR = os.path.join('..', 'data', 'processed')
MODEL_DIR = os.path.join('..', 'models')

# Initialize global constants to ensure model reproducibility and consistent test splitting
RANDOM_SEED = 42
TEST_SIZE = 0.2

def load_final_dataset():
    # Construct the file path for the combined final dataset ingestion
    data_path = os.path.join(PROCESSED_DATA_DIR, 'combined_final_dataset.csv')
    
    # Read the processed CSV into a pandas dataframe for modeling
    df = pd.read_csv(data_path)
    
    # Output the initial shape of the dataset for tracking
    print(f"Successfully loaded {df.shape[0]} records from {data_path}")
    
    # Return the loaded dataframe to the execution pipeline
    return df

def prepare_features(df):
    # Identify and remove records with missing or invalid target prices to ensure data quality
    df = df.dropna(subset=['price'])
    df = df[df['price'] > 0]
    
    # Log the volume of data remaining after initial cleaning
    print(f"Records remaining after target price filtering: {df.shape[0]}")

    # Drop the 'year' feature to eliminate multicollinearity with the 'age' feature
    if 'year' in df.columns:
        df = df.drop(columns=['year'])
        print("Dropped 'year' column to mitigate multicollinearity")
    
    # Construct a binary 'is_ev' flag to identify electric vehicles for specialized handling
    df['is_ev'] = (df['fuelType'] == 'electric').astype(int)

    # Calculate global medians for MPG and engine size from internal combustion (ICE) vehicles
    ice_mpg_med = df.loc[df['is_ev'] == 0, 'mpg'].median()
    ice_engine_med = df.loc[df['is_ev'] == 0, 'engineSize'].median()

    # Impute electric vehicle features with ICE medians to standardize the input space for the regressor
    df.loc[df['is_ev'] == 1, 'mpg'] = ice_mpg_med
    df.loc[df['is_ev'] == 1, 'engineSize'] = ice_engine_med
    
    # Log the imputation constants used for electric vehicle standardization
    print(f"Standardized EV features using ICE medians (MPG: {ice_mpg_med}, Engine: {ice_engine_med})")

    # Return the preprocessed dataframe along with imputation metadata for deployment
    return df, ice_mpg_med, ice_engine_med

def build_pipeline():
    # Identify high-cardinality categorical features requiring binary encoding
    high_card_features = ['make', 'model']
    
    # Initialize the ColumnTransformer to handle specialized binary encoding for specific features
    # Binary encoding decomposes the categorical labels into binary digits for tree-based efficiency
    preprocessor = ColumnTransformer(
        transformers=[
            ('binary_enc', BinaryEncoder(), high_card_features),
        ],
        remainder='passthrough'
    )
    
    # Output confirmation of the transformer configuration
    print(f"Constructed ColumnTransformer using BinaryEncoder for: {high_card_features}")

    # Construct a sequential pipeline to automate preprocessing, scaling, and model fitting
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('scaler', StandardScaler()),
        ('regressor', RandomForestRegressor(random_state=RANDOM_SEED, n_jobs=-1))
    ])

    # Return the uninitialized pipeline object for the search process
    return model_pipeline

def evaluate_performance(model, X, y, set_name="Test"):
    # Generate predictions using the fitted model pipeline to evaluate performance
    y_pred = model.predict(X)
    
    # Calculate standard regression metrics (MAE, RMSE, R2) to audit predictive power
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)
    
    # Output the calculated performance metrics to the console for verification
    print(f"\n--- {set_name} Performance ---")
    print(f"MAE:  ${mae:.2f}")
    print(f"RMSE: ${rmse:.2f}")
    print(f"R²:   {r2:.4f}")
    
    # Return the R2 score to facilitate variance checks and overfitting detection
    return r2

def run_training():
        # Ensure the target model directory exists before initiating the training process
        os.makedirs(MODEL_DIR, exist_ok=True)

        # Start the data preparation and stratified splitting phase
        # Load the master processed dataset and apply logic-based preprocessing
        dataset = load_final_dataset()
        dataset, mpg_med, engine_med = prepare_features(dataset)

        # Separate the feature matrix (X) from the target vector (y)
        X = dataset.drop(columns=['price'])
        y = dataset['price']

        # Perform a stratified split to ensure consistent EV representation across training and test sets
        X_train_raw, X_test_raw, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED, stratify=X['is_ev']
        )

        # Output the dimensions of the training and testing partitions
        print(f"Split data into Training ({X_train_raw.shape[0]}) and Testing ({X_test_raw.shape[0]}) partitions")

        # Apply One-Hot Encoding to low-cardinality features to prevent false ordinality in models
        low_card = ['country', 'transmission', 'fuelType']
        X_train = pd.get_dummies(X_train_raw, columns=low_card, drop_first=True)
        X_test = pd.get_dummies(X_test_raw, columns=low_card, drop_first=True)

        # Align training and testing feature sets to maintain consistent dimensionality
        X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)
        print(f"Final feature matrix contains {X_train.shape[1]} columns after One-Hot Encoding")

        # Calculate sample weights to prioritize predictive accuracy within the UK market
        weights = np.where(X_train_raw['country'] == 'uk', 4.0, 0.5)
        print("Computed sample weights (UK: 4.0, Other: 0.5) to prioritize regional accuracy")

        # Start the hyperparameter tuning and optimization phase
        base_pipeline = build_pipeline()

        # Define the search space for hyperparameter optimization to improve model stability
        params = {
            'regressor__n_estimators': [100, 200, 300],
            'regressor__max_depth': [10, 20, None],
            'regressor__max_features': ['sqrt', 1.0]
        }

        # Initialize RandomizedSearchCV with 5-fold cross-validation to find the optimal configuration
        search = RandomizedSearchCV(
            base_pipeline, params, n_iter=10, cv=5, 
            scoring='neg_mean_absolute_error', n_jobs=-1, random_state=RANDOM_SEED
        )

        # Execute the hyperparameter search using calculated sample weights for training
        print("Initiating RandomizedSearchCV optimization phase...")
        search.fit(X_train, y_train, regressor__sample_weight=weights)

        # Extract the best performing pipeline estimator for final assessment
        best_model = search.best_estimator_

        # Log the optimal parameters identified by the search process
        print(f"Optimization phase concluded. Best Parameters: {search.best_params_}")

        # Execute model assessment and overfitting audit
        train_r2 = evaluate_performance(best_model, X_train, y_train, "Training")

        # Evaluate the test set to verify generalization capability on unseen data
        test_r2 = evaluate_performance(best_model, X_test, y_test, "Testing")

        # Output the R2 variance to detect potential overfitting issues
        print(f"\nR² Variance (Train - Test): {train_r2 - test_r2:.4f}")

        # Perform robust cross-validation to verify model consistency across folds
        print("Executing 5-Fold Cross-Validation on the optimized model...")
        cv_scores = cross_val_score(best_model, X_train, y_train, cv=5, scoring='r2')

        # Output the mean R2 score and standard deviation across folds to verify stability
        print(f"Mean CV R²: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

        # Package the model, features, and imputation metadata into a deployment bundle
        bundle = {
            "pipeline": best_model,
            "non_ev_mpg_median": mpg_med,
            "non_ev_engine_median": engine_med,
            "feature_columns": list(X_train.columns)
        }

        # Save the deployment bundle to the model directory using joblib serialization
        save_path = os.path.join(MODEL_DIR, 'model.pkl')
        joblib.dump(bundle, save_path)

        # Output final verification confirmation to the console
        print(f"\nFinal Deployment Bundle saved successfully to: {save_path}")
if __name__ == "__main__":
    # Execute the pipeline
    run_training()
