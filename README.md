# Used Car Price Depreciation Analysis

## Business Understanding

### What is the problem?

Due to the uncertainty of vehicle valuation, Dealership and second-hand car platform often face a prominent financial risk when pricing used vehicles for trade-ins and resale, as the traditional method of valuing often relies on static "book values" or subjective experience (human intuition) rather than data-driven insights, which fails to account for dynamic market factors and complex non-linear relationships between variables.

#### Current challenges

- Diminishing profit margin due to over payment on Trade-in acquisition
- Overpriced vehicle leading to market stagnation as vehicles sit in inventories unsold beyond the turnover periods
- A lack of a standardized methodology accounting for the vehicle’s history leading to inconsistencies in evaluating the vehicles price
- Missed revenue opportunities from the inability to identify which vehicle types and brands retain value best
- Not accounting for the vehicles health condition during the pricing meaning reconditioning costs wipe out guaranteed margins when trade-in prices are set before mechanical inspection
- Multiple factors influence the pricing policy for used cars such as mileage, age, type (ICE or EV).
- Dealerships cannot reliably predict resale prices needed to maintain target profit margins
- Profit margins are difficult for car dealership to maintain as they cannot predict resale prices
- No clear evidence on whether electric vehicles depreciate differently than petrol vehicles
- Limited data in electric vehicles depreciation compared to internal combustion engine
- Electric Vehicle’s state of health are difficult to predict unlike ICE’s odometer which is visible resulting in losses in trading.
- Governments constantly subsidies electric vehicles using grants or tax credits giving a shock in the market resulting in sudden crashes overnight.

#### Valuation Gap

There is no robust predictive model that enables dealerships to input a vehicle's characteristics (mileage, year, brand, fuel type) and receive an accurate resale price prediction with confidence intervals meaning a dealership could offers too little for the vehicle and lose the trade-in customer to a competitor or they offer too much and erode their profit margin or incur a loss upon resale.

#### Market Complexity

Historical depreciation for Internal Combustion Engine (ICE) vehicles tend to follow a smoother depreciation curve that may not apply to EVs (due to battery degradation fears, tax incentives, or rapid tech obsolescence) due to ICE having a manufacturing warranty rather than EVs in which battery failure falls in the owner. These factors must be taken in mind due to the shift from ICE to EV in the automotive industry.

#### Brand Variety

Depreciation differs as premium and economy brands lose value at different rates. Treating them with the same depreciation model leads to pricing inefficiencies.

### What are the business objectives?

- **Profit Optimization:** Predict the resale price of a vehicle based on it’s attributes using a machine learning model allowing dealership and second hand car platforms to set offers that guarantees a specific profit margin.
- **Generate Actionable Insights:** Quantify the specific depreciation curves of different brands and, figure out what factors have the most prominent impact on resale value to optimally choose vehicles for inventory based on value perseverance.
- **Crafting a Purchasing Strategy:** Compare the resale stability of Petrol vs. Electric vehicles to decide if the dealership should pivot its inventory strategy toward or away from EVs based on current resale trends.
- **Develop a Prediction Model:** Formulate a predictive framework to ascertain vehicle resale values predicated on empirical insights derived from regression analyses of various attributes/features, thereby attaining a high level of predictive precision.
- **Identifying Depreciation Patterns:** Evaluate the reduction in the value of a vehicle in relation to features/attributes, contrast the rates of depreciation between internal combustion engine (ICE) vehicles and electric vehicles (EVs), and ascertain the brands that maintain the highest residual value.
- **Pricing Clarity:** Ensure clarity regarding the elements that affect the pricing of vehicles (for instance, being equipped to elucidate to a customer the rationale behind their vehicle's lower valuation).

### What is the success criteria?

#### **Business Success Criteria:**

- **Secure Targeted Profit Margins:** Eliminate excessive compensation by implementing a pricing model that ensures a baseline gross profit margin of no less than ten percent upon the resale.
- **Capture Valuation Factors:** Identify the attributes with the most noticeable impact on the vehicle’s resale price wither it is for internal combustion engines (odometer) or electric vehicles (battery health).
- **Evaluate Vehicle Realistically:** Utilize a data-driven pricing methodology as opposed to depending on subjective “expertise” or a uniform valuation, while accounting for variables that are not linearly quantifiable.
- **Coping with Market Shocks:** Adjust pricing strategies, especially concerning electric vehicles, to alleviate financial risk stemming from sudden market variances, such as immediate modifications in government subsidies.

#### **Data Mining Success Criteria:**

- **Prediction Accuracy:** Attain a Root Mean Squared Error (RMSE) or a Mean Absolute Percentage Error (MAPE) that is low to ensure commercial viability.
- **Variance Explained:** Secure an $R^2$ score exceeding $0.80$, demonstrating that the model accounts for no less than 80% of the variance in pricing as determined by the available features.
- **Being Actionable:** The model must demonstrate it’s performance on unseen data to ensure it isn't memorizing specific car listings which is evaluated by the metrics mentioned above.
- **Model Deployment:** The trained model is implemented with an interface that enables dealerships to input the characteristics of the vehicles and receive the predicted resale price.

### Current resource availability

#### Personnel

- **Data Analyst:** The data scientist, responsible for the data analysis and model’s development.
- **Project Supervisor:** Available for high-level guidance, validation of methodology, and project oversight.

#### Data

- **Primary Source(s):** Kaggle Used Car Datasets
    - **Format:** Structured data in .csv format.
    - **Volume:** Approximately 10000+ records.
    - **Features:** Year, Model, Price, Transmission, Mileage, FuelType, Tax, MPG, EngineSize.
- **Data Constraints:**
    - **Static Nature:** The data is historical and does not reflect real-time market fluctuations (e.g., sudden price spikes due to supply chain shortages).
    - **EV Representation:** There is a risk that the dataset is heavily skewed towards Internal Combustion Engine (ICE) vehicles. Finding sufficient data points for Electric Vehicles (EVs) to make statistically significant comparisons may be a challenge.

#### Computing resources

- Personal Laptop: 16 GB RAM
    - *Suitability:* Sufficient for data cleaning, exploratory analysis, and training standard regression models which fit for the purposes of this project.
- Google Colab
    - *Usage:* To be used if the dataset size causes memory issues on the local machine or if models require GPU acceleration for faster training.

Minimum Requirements:

- Laptop with at least 8 GB RAM
- 10-20 GB of free storage

#### Software

- **Programming Languages:** Python (Primarily For Regression Models) & R (For Data Analytics).
- **Environment:** Jupyter Notebooks/VS Code and RStudio.
- **Libraries/Packages:**
    - *Data Manipulation:* pandas, numpy (for handling tabular data).
    - *Visualization:* matplotliv, seaborn (for plotting depreciation curves).
    - *Modeling:* scikit-learn (for regression and machine learning algorithms).
- **Version Control:** Git + GitHub
- **Documentation:** Notion
- **Presentation + Poster:** Canva

### Requirements, Assumptions, and Constraints

#### Requirements

- **Project Deliverables:** A detailed report adhering to the CRISP-DM methodology, an A3 poster, along with a Jupyter Notebook encompassing all code, visualizations, and interpretations of the model.
- **Modelling Requirement:** The proposed solution is required to implement a minimum of three distinct regression models for the purpose of performance comparison and identification of the most effective predictor for resale value.
- **Analysis Requirement:** The project is mandated to explicitly evaluate the hypothesis that "Electric Vehicles depreciate at a faster or different rate compared to Petrol vehicles.”
- **Metric Requirement:** The final model must incorporate suitable error metrics ($RMSE$, $MAE$, $R^2$) in order to quantify the "guaranteed profit margin" for dealerships.
- **Data Cleaning:** The raw dataset undergoes a cleansing process to eliminate outliers, thereby ensuring that the analysis accurately reflects the market conditions.
- **Visualizations**: A minimum of 5 charts must be provided in the report and presentations.

#### Assumptions

- **Market Stability:** The analysis presumes the dataset reflects a period of economic stability, where the relationships among Year, Mileage, and Price remain steady and are not influenced by short-term disruptions such as the semiconductor shortages seen between 2021 and 2022.
- **Data Integrity:** It is assumed that the "Price" values in the dataset correspond to legitimate market transactions, excluding cases involving distressed sales (such as vehicles sold for parts) or misleading listings.
- **Market & Price Stability:** Market conditions remain stable during analysis period and Prices reflect actual transaction values, not asking prices.
- **Linear/Monotonic Relationships:** It is assumed that for the majority of the vehicles, as both mileage and age increase, the price concurrently diminishes. Although the rate of this alteration may fluctuate, the direction of the relationship is assumed to be negative.
- **Proxy Variables:** Since we likely lack a specific "Battery Health" column for EVs, we assume that year and milage act as sufficient proxies for battery degradation.
- **Uniform Depreciation Trends:** The patterns of depreciation are uniform across various regions, and Outliers are considered to signify market anomalies rather than mere data inaccuracies.
- **Verified Mileage Accuracy:** Mileage readings are accurate and verified, representing the true mechanical usage of the vehicle without tampering.
- **Dealer Profit Standardization:** Dealerships aim for at least a 10% profit margin on car resales, establishing a predictable correlation between acquisition costs and the prices at which they are listed.

#### Constraints

- **Missing Features:** A clear limitation is the absence of a variable such as "Vehicle Condition" or "Accident History." In practical situations, the presence of a scratch or dent substantially influences a vehicle's valuation. Our model is restricted to valuing "average condition" cars.
- **Temporal Relevance:** The dataset is historical. A predictive model developed utilizing data from a specific time frame and may not accurately forecast prices in current times due to factors such as inflation and the introduction of new vehicle models.
- **Geographic Bias:** Should the dataset originate from a specific country, implications of the findings, are limited to that particular geographic area and may not be applicable on a global scale.
- **EV Data Scarcity:** Electric Vehicles often constitute less than 5% of the dataset, adversely  resulting in broader confidence intervals and increased uncertainty relative to ICE vehicles.
- **Static Models:** The model lacks real-time market data integration, rendering it ineffectual in accounting for price variations precipitated by changes in consumer demand or auction trends.
- **Economical Factors Exclusion:** The analysis neglects external variables like inflation, fuel prices, or interest rates, which substantially impact vehicle affordability and market volume.

### Risks and contingencies

#### Technical Risks

1. **Poor model performance**
    - **Likelihood:** Medium
    - **Impact:** High
    - **Contingency:**
2. **Insufficient EV data**
    - **Likelihood:** High
    - **Impact:** Medium
    - **Contingency:** Combine hybrid vehicles, reduce scope to brand-only analysis
3. **Multicollinearity issues (Mileage vs Year)**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:**
4. **Overfitting**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:** Cross-validation, early stopping, simpler models
5. **Missing/wrong data**
    - **Likelihood:** High
    - **Impact:** High
    - **Contingency:** EDA, multiple imputation strategies, sensitivity analysis

### Project Risks

1. **Tight deadline**
    - **Likelihood:** High
    - **Impact:** High
    - **Contingency:** Prioritize simpler models first
2. **Software/environment issues**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:** Use Google Colab, version control
3. **Scope creep**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:** Strictly adhere to project requirements
4. **Dataset unavailability**
    - **Likelihood:** Low
    - **Impact:** Critical
    - **Contingency:** Use region/brand specific datasets

### Business Logic Risks

1. **Wrong profit margin assumptions**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:** Test multiple margin scenarios (10%, 15%, 20%)
2. **Changing Market conditions**
    - **Likelihood:** High
    - **Impact:** Medium
    - **Contingency:** Mentioned in business requirement
3. **External factors not captured**
    - **Likelihood:** High
    - **Impact:** Low
    - **Contingency:** Mentioned in business requirement, suggested for future implementation

### Costs and benefits

**Costs**

- **Development Time:** The primary expense pertains to the duration necessitated for data cleaning, exploratory analysis, and the development of the predictive model.
- **Compute Resources:** The financial implications are minimal as the analysis and training are being done on either a personal laptop or a cloud provider which offers free tier service suitable for the project.
- **Model Maintenance:** In practical applications, this model would necessitate quarterly retraining to account for new car models and adapt to fluctuation economic conditions.

**Benefits**

- **Reduced Overpayment:** Dealerships could diminish acquisition overpayment by identifying overpriced units during the trade-in.
- **Faster, more consistent pricing decisions:** This approach eradicates human biases, guaranteeing that each trade-in is assessed properly.
- **Guaranteed Profit Margins:** The model calculates a "Maximum Buy Price" by automatically subtracting target margins and refurbishing costs from the predicted retail price, ensuring profitability.
- **Scalability:** Allows the dealership to analyze numerous auction listings or trade-in requests concurrently, a scale of operation that is impossible to match with traditional methods.

### Data mining goals

1. **Primary Goals**
   - Price Prediction Model Development (5+ regression models, R² ≥ 0.80)
   - Profit Margin Prediction Framework (10% margin calculator)
   - Petrol vs. EV Depreciation Comparison (statistical hypothesis testing)
2. **Secondary Goals**
   - Brand Value Retention Analysis (Toyota vs BMW comparison)
   - Feature Importance Analysis (mileage, year, brand impact)
   - Depreciation Pattern Discovery (linear vs non-linear)
   - Data Quality Assessment

## Data Understanding

### Initial data collection

The initial data collection process involved gathering used car data from two public kaggle datasets to create a diverse data collection:

1. **100,000 UK Used Car Data set**: 11 individual CSV files separated by car manufacturer. (These were collected and concatenated into a single dataset)
2. **Used Cars Dataset (Andrei Novikov)**: A broader source of used car listings containing the same features as the 100,000 UK Used Car Dataset.

### Data description

Across the two datasets, the core focus was to extract and standardize nine features consisting of:

- **make**: The brand or manufacturer of the car.
- **model**: The specific model of the car.
- **year**: The manufacturing or registration year of the vehicle.
- **mileage**: The total distance the car has been driven.
- **transmission**: The type of gearbox.
- **fuelType**: The type of fuel the vehicle consumes (e.g., Petrol, Diesel, Hybrid, Electric).
- **mpg**: Miles per gallon, representing the vehicle's fuel efficiency (not applicable for EVs).
- **engineSize**: The engine capacity in liters (not applicable for EVs).
- **price**: The target variable, representing the listed selling price of the used car.

### Data exploration

During the data exploration, several discrepancies across the two data sources were identified which necessitated standardizing the formats prior to merging:

- **Inconsistent Naming conventions**: The same car makes were represented differently across datasets (e.g., merc or cclass instead of mercedes-benz, and vw instead of volkswagen).
- **Complex Strings & Nested Data**: Models in some datasets contained extra information that needs stripping.
- **Compound Variables**: Important numerical values like engineSize and mpg were located within text strings and needs to be extracted.
- **Categorical Variations**: Transmission and Fuel Type fields had several labels with the same meaning (e.g., M/T vs Manual, Premium vs Petrol) that needs grouping into standardized categories.

### Data quality

The data quality assessment highlighted a few issues that were directly addressed during the cleaning and integration pipelines:

- **Irrelevant/Redundant Features**: Tax columns were dropped as they were not consistently available or relevant across all datasets.
- **Missing Values**: Missing values or formatting errors that resulted in null objects were dropped from the final unified dataset.
- **Duplication Risk**: Combining multiple data sources created a chance of having identical rows, which we found and removed using the pandas de-duplication tool to prevent data leakage and biased models.
- **Formatting and Typing Consistency**: Applying lower and title casing, along with converting extracted text into numerical types like floats for engine size and mpg, and organizing columns into a specific order ensured the structural quality and consistency of the combined dataset.

# Data Preparation

## **Rationale for inclusion/exclusion**

| **Feature** | **Decision** | **Rationale** |
| --- | --- | --- |
| make | **Included** | Buyers pay different amounts depending on the manufacturer. |
| model | **Included** | The specific car model dictates the baseline price. |
| year | **Included** | Age dictates how much value a car loses over time. |
| mileage | **Included** | Buyers look at the odometer to judge wear and tear. |
| transmission | **Included** | People have strong preferences for manual or automatic gearboxes. |
| fuelType | **Included** | Running costs change based on the fuel the car needs. |
| mpg | **Included** | Fuel efficiency changes the long term ownership cost. |
| engineSize | **Included** | Bigger engines mean higher insurance premiums and performance expectations. |
| price | **Included** | We use this target variable to build the predictive model. |
| tax / tax(£) | **Excluded** | Missing data across the sources creates formatting problems. |
| engine (raw string) | **Excluded** | We pulled the numerical data out to make a new column. |

## **Derived attributes**

- **make (UK dataset):** The dataset originally came in separate files for each car brand without a brand column. File names were used to create the brand names.
- **engineSize (Andrei Novikov dataset):** Engine size data is buried inside text descriptions. The numbers pulled out to create a clean numerical column for engine capacity.
- **mpg (Andrei Novikov dataset):** Fuel economy as a range between two numbers. The average of those two numbers were taken to get a single value for each car.
- **model (Andrei Novikov dataset):** Car model names contained extra data and engine specifications. The first word were only kept to group similar cars together cleanly.

## **Generated records**

No synthetic or artificially generated records were introduced into the dataset. All rows in the final combined dataset originate directly from the three source datasets. The only record-level operations performed were filtering (removing rows with missing price values) and de-duplication (removing exact duplicate entries introduced during the merging process).

## **Merged data**

The three independently processed datasets were merged through vertical concatenation (row-wise) into a single unified DataFrame:

1. **Feature renaming** was performed first — all three datasets were transformed to share an identical set of nine columns with consistent naming across the two datasets (e.g., manufacturer → make, fuel_type → fuelType).
2. **Concatenation** was then carried out using pd.concat() with ignore_index=True, ensuring a continuous integer index across the combined dataset.
3. **De-duplication** was applied using drop_duplicates() to remove any exact duplicate rows that may have appeared across the overlapping source datasets.
4. **Null removal** was performed as a final step — any rows where the price column was null after merging were dropped to ensure every record in the final dataset has a valid prediction target.

## **Reformatted data**

- **Consistent Casing:** All make values were converted to lowercase; fuelType values were converted to title case; and transmission values were capitalised — making the data match across all the different sources.
- **Standardised Category Labels:** Overlapping categorical values were mapped to a single label (e.g., Gasoline / Premium → Petrol; manual / m/t → Manual).
- **Numerical Type Casting:** Derived features (engineSize, mpg) were explicitly stored as float types rather than left as strings.
- **Column Ordering:** All datasets were re-indexed to a fixed column order (make, model, year, mileage, transmission, fuelType, mpg, engineSize, price) before and after merging, ensuring structural consistency.
- **Export:** The final combined dataset was exported to CSV with index=False, producing a file (combined_final_dataset.csv) ready for modelling.
