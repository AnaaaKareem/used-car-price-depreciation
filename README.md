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
