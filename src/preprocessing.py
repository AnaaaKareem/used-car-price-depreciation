# Import standard libraries for data manipulation, numerical operations, and system path management
import pandas as pd
import numpy as np
import glob
import os
import re

# Define relative directory paths for raw and processed data ingestion
RAW_DIR = os.path.join('..', 'data', 'raw')
PROCESSED_DIR = os.path.join('..', 'data', 'processed')

def load_uk_dataset():
    # Construct search path for all UK dataset CSV files using a glob pattern
    uk_path = os.path.join(RAW_DIR, '100,000 UK Used Car Data set', '*.csv')
    
    # Extract file list using the constructed directory-wide pattern matching
    files = glob.glob(uk_path)
    
    # Initialize a list to store individual make dataframes before concatenation
    dfs_uk = []

    # Iterate through identified files to read and assign vehicle makes
    for f in files:
        # Read the current CSV file into a temporary dataframe
        temp_df = pd.read_csv(f)
        
        # Extract filename without the extension to identify the vehicle make
        file_name = os.path.basename(f).split('.')[0]
        
        # Assign the identified make to the temporary dataframe as a new feature
        temp_df['make'] = file_name
        
        # Set 'uk' as the country feature to differentiate records in the integrated dataset
        temp_df['country'] = 'uk'
        
        # Append the temporary dataframe to the collection list
        dfs_uk.append(temp_df)

    # Concatenate all collected dataframes into a single master UK dataset
    df_uk = pd.concat(dfs_uk, ignore_index=True)
    
    # Return the unified UK dataframe for the processing pipeline
    return df_uk

def load_andrei_dataset():
    # Construct the file path for the Andrei Novikov dataset repository
    andrei_path = os.path.join(RAW_DIR, 'Used Cars Dataset Andrei Novikov', 'cars.csv')
    
    # Read the target CSV file into a pandas dataframe
    df_an = pd.read_csv(andrei_path)
    
    # Assign 'usa' as the country feature to maintain consistency with the UK dataset
    df_an['country'] = 'usa'
    
    # Return the loaded Andrei dataset for standardization
    return df_an

def load_scraped_ev_dataset():
    # Define the specific filename for the newly scraped UK EV dataset
    scraped_filename = 'auto_trader_uk_scraped_cars_20260331_200824.csv'
    scraped_path = os.path.join(RAW_DIR, scraped_filename)
    
    # Read the scraped CSV file into a pandas dataframe
    df_scraped = pd.read_csv(scraped_path)
    
    # Assign 'uk' as the country feature to ensure alignment during integration
    df_scraped['country'] = 'uk'
    
    # Return the raw scraped dataframe for specialized cleaning
    return df_scraped

def extract_engine_size(engine_str):
    # Check for null values to avoid regex errors
    if pd.isna(engine_str): 
        return np.nan
        
    # Identify numerical engine size from strings using regular expressions (e.g., '2.0L')
    match = re.search(r'(\d+\.?\d*)\s*L', str(engine_str))
    
    # Return extracted float value if a valid pattern match is found
    if match:
        return float(match.group(1))
        
    # Return null if the string format is unrecognized or invalid
    return np.nan

def parse_mpg(mpg_str):
    # Check if the input value is missing
    if pd.isna(mpg_str): 
        return np.nan
        
    # Split the string by hyphen to handle range values and identify numerical parts
    parts = str(mpg_str).split('-')
    try:
        # Convert split parts into a list of floats for calculation
        values = [float(p) for p in parts]
        
        # Calculate and return the mean of the identified values to standardize the feature
        return sum(values) / len(values)
    except: 
        # Return null if float conversion fails during parsing
        return np.nan

def impute_mode(group):
    # Check if a valid mode actually exists for the specific make/model combination
    if not group.mode().empty:
        # Fill null values with the most frequent value (mode) in the group
        return group.fillna(group.mode()[0])
        
    # Return 'Unknown' label if no mode is present for the group to maintain data integrity
    return group.fillna("Unknown")

def impute_median(group, global_median):
    # Check if there is at least one numeric value available to calculate a median
    if group.notna().any():
        # Fill nulls with the specific median of the grouped features
        return group.fillna(group.median())
        
    # Return the global median if the entire group is null to ensure no missing values remain
    return group.fillna(global_median)

def run_preprocessing():
        # Initialize the processed data directory if it does not already exist
        os.makedirs(PROCESSED_DIR, exist_ok=True)

        # Execute the data audit phase to identify initial data quality issues and dimensions
        print("Starting Data Audit...")
        raw_uk = load_uk_dataset()
        raw_an = load_andrei_dataset()
        raw_scraped = load_scraped_ev_dataset()

        # Identify initial null counts and dataset dimensions for the audit report
        print(f"UK Raw Shape: {raw_uk.shape} | Nulls: {raw_uk.isnull().sum().sum()}")
        print(f"Andrei Raw Shape: {raw_an.shape} | Nulls: {raw_an.isnull().sum().sum()}")
        print(f"Scraped EV Raw Shape: {raw_scraped.shape} | Nulls: {raw_scraped.isnull().sum().sum()}")

        # --- Clean Scraped EV Dataset (Specialized Logic) ---
        # Normalize the model column by stripping whitespace and converting to lowercase
        raw_scraped['model'] = raw_scraped['model'].astype(str).str.lower().str.strip()

        # Resolve the 'make/model' shift by extracting the first word as the vehicle make
        raw_scraped['make'] = raw_scraped['model'].str.split(' ').str[0].str.capitalize()

        # Reconstruct the 'model' feature by joining all subsequent words in the string
        raw_scraped['model'] = raw_scraped['model'].str.split(' ').str[1:].str.join(' ').str.capitalize()

        # Handle instances where the model extraction results in an empty string
        raw_scraped['model'] = raw_scraped['model'].replace('', 'Unknown')

        # --- Standardize and Clean Integrated Data ---
        # Perform currency conversion to USD (UK 2020: 1.284 | Scraped 2026: 1.32)
        raw_uk['price'] = raw_uk['price'] * 1.284
        raw_scraped['price'] = raw_scraped['price'] * 1.32

        # Convert imperial MPG to US standards for all UK-sourced records
        raw_uk['mpg'] = raw_uk['mpg'] * 0.8327
        raw_scraped['mpg'] = raw_scraped['mpg'] * 0.8327

        # Construct the 'age' feature relative to each dataset's specific temporal context
        raw_uk['age'] = 2020 - raw_uk['year']
        raw_an['age'] = 2023 - raw_an['year']
        raw_scraped['age'] = 2026 - raw_scraped['year']

        # Rename features in the Andrei dataset to match the standardized master schema
        raw_an = raw_an.rename(columns={"manufacturer": "make", "fuel_type": "fuelType"})

        # Apply regular expression parsing to Andrei engine and MPG features
        raw_an['engineSize'] = raw_an['engine'].apply(extract_engine_size)
        raw_an['mpg'] = raw_an['mpg'].apply(parse_mpg)

        # Define a master column order to ensure structural consistency during concatenation
        ordered_columns = ['country', 'make', 'model', 'year', 'age', 'mileage', 'transmission', 'fuelType', 'mpg', 'engineSize', 'price']

        # Filter and reorder dataframes to match the master column schema
        raw_uk = raw_uk[ordered_columns]
        raw_an = raw_an[ordered_columns]
        raw_scraped = raw_scraped[ordered_columns]

        # Combine all cleaned datasets into a unified master dataframe
        final_df = pd.concat([raw_uk, raw_an, raw_scraped], ignore_index=True)

        # Execute final cleaning by removing duplicates and unrealistic outliers
        final_df.drop_duplicates(inplace=True)
        final_df = final_df[final_df['price'] >= 500]
        final_df = final_df[
            ((final_df['engineSize'] <= 6.0) & (final_df['engineSize'] >= 1.0)) |
            (final_df['fuelType'] == 'electric') |
            (final_df['fuelType'] == 'hybrid')
        ]
        final_df = final_df.dropna(subset=['price', 'age', 'mileage'])

        # Apply grouped mode imputation to categorical features (transmission, fuelType)
        for col in ['transmission', 'fuelType']:
            final_df[col] = final_df.groupby(['make', 'model'])[col].transform(impute_mode)

        # Apply grouped median imputation to numerical features using global medians as fallback
        for col in ['engineSize', 'mpg']:
            global_med = final_df[col].median()
            final_df[col] = final_df.groupby(['make', 'model'])[col].transform(lambda x: impute_median(x, global_med))

        # Drop any remaining records that could not be resolved through imputation
        final_df = final_df.dropna()

        # Calculate initial memory usage for the optimization report
        initial_mem = final_df.memory_usage(deep=True).sum() / 1024**2

        # Downcast numerical features to 32-bit floating point and integer precision
        final_df[['mileage', 'mpg', 'engineSize', 'price']] = final_df[['mileage', 'mpg', 'engineSize', 'price']].astype('float32')
        final_df[['year', 'age']] = final_df[['year', 'age']].astype('int32')

        # Convert high-cardinality and structural strings to the 'category' data type
        cat_cols = ['country', 'make', 'model', 'transmission', 'fuelType']
        final_df[cat_cols] = final_df[cat_cols].astype('category')

        # Calculate final memory usage to verify optimization efficiency
        final_mem = final_df.memory_usage(deep=True).sum() / 1024**2

        # Export the finalized, optimized dataset to the processed directory
        output_path = os.path.join(PROCESSED_DIR, 'combined_final_dataset.csv')
        final_df.to_csv(output_path, index=False)

        # Output final verification and memory optimization summary
        print(f"\nPipeline Complete.")
        print(f"Memory Reduced: {initial_mem:.2f} MB -> {final_mem:.2f} MB")
        print(f"Final Dataset: {len(final_df)} records saved to: {output_path}")
if __name__ == "__main__":
    # Execute the pipeline
    run_preprocessing()
