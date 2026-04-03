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
    - **Volume:** Approximately 680,000+ records across all merged sources (108,540 UK listings, 762,091 Andrei Novikov records, plus AutoTrader EV scraped entries).
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

- **Programming Languages:** Python (Primarily For Regression Models, Data Analytics, and API development).
- **Environment:** Jupyter Notebooks/VS Code and RStudio.
- **Libraries/Packages:**
    - *Data Manipulation:* pandas, numpy (for handling tabular data).
    - *Visualization:* matplotlib, seaborn (for plotting depreciation curves).
    - *Modeling:* scikit-learn (for regression and machine learning algorithms).
- **Version Control:** Git + GitHub
- **Documentation:** Notion
- **Presentation + Poster:** Canva

### Requirements, Assumptions, and Constraints

#### Requirements

- **Project Deliverables:** A formalized report adhering to the CRISP-DM methodology, an A3 poster, along with a Jupyter Notebook exclusively charting all programmatic algorithms, visualizations, and interpretations of the model.
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
    - **Contingency:** Evaluate multiple regression architectures simultaneously, apply cross-validation, and perform hyperparameter tuning via Randomized Search CV to extract maximum performance from each candidate.
2. **Insufficient EV data**
    - **Likelihood:** High
    - **Impact:** Medium
    - **Contingency:** *Resolved* — A Playwright-driven automated web scraper (`scraper.py`) was implemented to continuously extract live Electric Vehicle listings from AutoTrader UK, directly addressing the EV representation gap.
3. **Multicollinearity issues (Mileage vs Year)**
    - **Likelihood:** Medium
    - **Impact:** Medium
    - **Contingency:** Utilize tree-based ensemble methods (e.g., Random Forest) which are inherently robust to multicollinearity, and derive the composite `age` feature to consolidate the year dimension.
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

According to the analytical objectives, The initial data collection process involved gathering used vehicle data from diverse public and newly scraped sources to create an expansive repository:

#### 100,000 UK Used Car Data set
The framework incorporated 108,540 entries distributed across manufacturer-specific files.

#### Used Cars Dataset (Andrei Novikov)
This expansive source was utilized to contribute 762,091 records predominantly from the American market.

#### AutoTrader UK Scraped Dataset
A recently acquired dataset pertaining to Electric Vehicles (EVs) was scraped explicitly, in turn augmenting the EV representation within the broader Internal Combustion Engine (ICE) pool.

For the foreseeable future, this diversified compilation delivers a formidable baseline for subsequent regression modelling.

### Data description

The collected data relies on multiple individual sources possessing a myriad of diverse features and structural layouts. Consequently, The specific documentation of features across each utilized dataset is presented as follows:

#### 100,000 UK Used Car Data set (10 Features)
- **make**: The manufacturer brand dictating general market perception.
- **model**: The specific vehicle classification establishing baseline evaluations.
- **year**: The manufacturing timeline driving chronological depreciation.
- **price**: The listed market valuation explicitly required for targeting.
- **transmission**: The gearbox typology dictating operational engagement.
- **mileage**: The explicit odometer reading demonstrating accrued real-world wear.
- **fuelType**: The primary chemical energy mechanism utilized.
- **tax**: The corresponding local governmental duty requirement imposed.
- **mpg**: The numerical volume expressing fuel efficiency structurally.
- **engineSize**: The formalized volumetric capacity of the combustion engine.

#### Used Cars Dataset (Andrei Novikov) (20 Features)
- **manufacturer**: The production entity generating the subject vehicle.
- **model**: The formally designated automobile structure.
- **year**: The officially documented registration framework.
- **mileage**: The gross functional distance effectively traveled.
- **engine**: A complex textual string encapsulating numerical specifications and configuration layouts identically.
- **transmission**: The implemented gear shifting mechanism organically recorded.
- **drivetrain**: The mechanical orientation systematically routing power to specific wheel axles.
- **fuel_type**: The specifically designated categorical fuel prerequisite.
- **mpg**: A textual string stipulating lower and upper boundaries of fuel consumption ranges.
- **exterior_color**: The explicitly documented external visualization.
- **interior_color**: The internal upholstery configuration.
- **accidents_or_damage**: A recorded marker formally pinpointing prior physical compromises or events.
- **one_owner**: An indicator dictating if the unit was securely retained by a solitary entity.
- **personal_use_only**: A declaration systematically clarifying the absence of a commercial timeline.
- **seller_name**: The recognized commercial title designated definitively to the vendor.
- **seller_rating**: An autonomous numerical quantification detailing vendor reliability transparently.
- **driver_rating**: The perceived qualitative evaluation organically sourced from automotive operators.
- **driver_reviews_num**: The accrued volumetric scale of documented consumer reviews.
- **price_drop**: A quantifiable tracking of past financial reductions decisively implemented prior to current listings.
- **price**: The finalized monetary sum explicitly dictated by the holding vendor.

#### AutoTrader UK Scraped Dataset (Electric Vehicles)
While structured dynamically post-scraping, this supplementary asset natively mimics core elements required for subsequent identical integrations:
- **model**: A compound textual string prominently containing both the broad brand and specific vehicle model collectively.
- **year**: The formally recorded chronological origin.
- **mileage**: The mechanical distance documentation accrued.
- **transmission**: The automated gear infrastructure inherently native to comprehensive electrical units.
- **fuelType**: Consistently isolated structurally as an electrical classification.
- **mpg**: Provided selectively as an electrical economy conversion equivalent.
- **engineSize**: Often structurally absent or recorded minimally owing explicitly to the absence of internal combustion cylinders.
- **price**: The contemporary market offering dynamically scraped yielding modern valuation insights.

### Data exploration

During the analytical assessment, Disparate matrices were interrogated systematically to extract baseline statistical variances prior to integration.

#### UK Dataset Insights

**Univariate Analysis:**
- **Distribution Skewness:** Price and mileage distributions displayed severe right-skewed topologies natively, indicating that the vast majority of available inventory clusters around lower valuation thresholds and moderate mechanical wear (`price_milage_dist_uk.png`).
- **Categorical Dominance:** Evaluating mechanical typologies prominently revealed that manual transmissions and petrol-based combustion architectures dominate the historical UK marketplace (`transmission_fuelType_dist_uk.png`).
- **Brand Frequency:** Manufacturer frequency matrices indicated that domestic and mainstream European brands (e.g., Ford, Volkswagen, Vauxhall) encompass the largest structural volume within the localized grouping (`make_model_analysis_uk.png`).

**Multivariate Analysis:**
- **Value Depreciation:** Hexbin and scatter plot frameworks mathematically verified a formidable negative correlation between accumulating mileage and pricing retention, specifically displaying dense clusters at lower thresholds (`price_milage_uk.png`, `hex_price_milage_uk.png`).
- **Feature Correlation:** The localized correlation heatmap quantitatively confirmed that vehicle age and recorded mileage exert the absolute strongest detrimental impact structurally upon the target price (`heatmap_uk.png`).
- **Categorical Valuation:** Brand-specific distributions established unequivocally that premium manufacturers (e.g., Audi, BMW) inherently command higher median valuations structurally compared to their mainstream counterparts (`price_dist_make_uk.png`). Furthermore, Automatic architectures consistently demonstrated superior pricing resilience empirically over manual constraints (`price_transmission_uk.png`).

#### Andrei Novikov Dataset Insights

**Univariate Analysis:**
- **Damage Representation:** Evaluating historical accident markers utilizing pie chart distributions confirmed that an overwhelming majority of listings naturally lack prior physical compromises organically (`accident_pie_andrei.png`).
- **Distribution Topography:** Identical to the UK observations, foundational price and mileage vectors presented expansive right-tailed distributions mathematically (`price_milage_dist_andrei.png`).
- **Mechanical Formats:** Unlike the European dataset, the American matrices exhibited sheer dominance regarding automatic transmission typologies alongside gasoline-focused propulsion structures (`transmission_fuelType_andrei.png`).

**Multivariate Analysis:**
- **Accident Penalization:** Scatter and boxplot arrays dictated that isolated accident history records actively initiate severe financial deterioration, penalizing the inherent valuation abruptly (`price_accident_andrei.png`).
- **Depreciation Curves:** Mileage-based scatter metrics visually plotted non-linear depreciation curves strictly, wherein valuation decays aggressively during initial ownership phases prior to stabilizing dynamically (`price_milage_andrei.png`, `hex_price_milage_andrei.png`).
- **Structural Collinearity:** The corresponding heatmap architecture natively highlighted strong interdependencies connecting manufacturing years alongside mileage explicitly, further necessitating systemic downstream regularization (`heatmap_andrei.png`).

#### Structural Discrepancies

Additionally, A myriad of structural discrepancies traversing the divergent datasets were flagged which dictated standardization systematically:
- **Inconsistent Naming Conventions:** Brand configurations were evaluated meticulously against the UK baseline, subsequently demonstrating acute formatting inconsistencies specifically impacting the Andrei Novikov grouping (e.g., `merc` actively recorded instead of `mercedes-benz`).
- **Complex Nested Strings:** Specifically across the unrefined Andrei listings and the freshly acquired AutoTrader EV framework, models fundamentally grouped engine displacements within the name, explicitly demanding rigorous stripping.
- **Compound Variables:** Important numerical values like engine size measurements within the Andrei Novikov dataset were originally located within extensive text strings and explicitly required targeted regex extraction operations.
- **Categorical Variations:** Identical transmission labels functionally possessed disjoint nomenclature (e.g., `M/T` natively versus `Manual`), firmly demanding strict unified categorical matching. 

### Data quality

The comprehensive data quality assessment highlighted extensive issues that were methodically addressed during the rigorous cleaning pipelines:

- **Irrelevant/Redundant Features**: Tax columns natively restricted strictly to the UK observations were dropped prominently, as they were not consistently available.
- **Missing Values**: Missing values or formatting errors that resulted in null objects structurally across all groupings were systematically dropped from the final unified dataset.
- **Duplication Risk**: Combining multiple structures organically induced duplication. According to statistical assessments, the standard UK dataset contained 2.09% duplicate observations, while the Andrei Novikov grouping exhibited 1.20% duplication metrics. These components were subsequently eradicated seamlessly.
- **Formatting and Typing Consistency**: The Andrei Novikov file displayed substantial missing voids inside detailed categorical spheres structurally. Furthermore, The unstructured AutoTrader EV dataset necessitated immediate textual normalization to structurally decouple successfully joined brand identities. Consequently, Strategic extraction, dropping of non-essential variables heavily burdened by null distributions, and stringent grouping matching the UK standard were formulated as a prominent priority. For the foreseeable future, Adhering to these strict quality thresholds will guarantee robust implementation of predictive evaluations.

# Data Preparation

## **Rationale for inclusion/exclusion**

In the context of the preparation pipeline, A meticulously strict protocol was utilized to filter disparate variables dynamically. Firstly, Key variables such as brand (make), model, manufacturing year, mileage accumulation, specific transmission format, fuel framework (fuelType), miles per gallon (mpg), engine capacity (engineSize), alongside the targeted price, were collectively maintained, owing to their prominent influence over resale valuation. On the contrary, Columns pertaining to tax evaluations or excessively detailed dimensions found in the Andrei Novikov dataset—like seller ratings or interior aesthetic color—were excluded outright. Hence, Diminishing superfluous features aids analytical efforts by systematically stripping noise, in turn yielding clarity.

| **Feature** | **Decision** | **Rationale** |
| --- | --- | --- |
| make | **Included** | Diverse manufacturers dictate distinct market valuations objectively. |
| model | **Included** | The designated vehicle model establishes a formidable baseline price threshold. |
| year | **Included** | Age functions as a prominent factor driving depreciation trajectories over time. |
| mileage | **Included** | The odometer measurement demonstrates accrued mechanical wear realistically. |
| transmission | **Included** | Consumer inclinations distinctly gravitate towards either manual or operational automatic gearboxes. |
| fuelType | **Included** | Operating and ongoing requirements escalate distinctly depending on the fuel mechanisms utilized. |
| mpg | **Included** | Volatile fuel efficiency measurements alter long-term ownership expenditures. |
| engineSize | **Included** | Expanded engine designs consistently correlate with augmented performance standards and insurance evaluations. |
| price | **Included** | This overarching metric is utilized as the primary target variable for crafting predictions. |
| tax / tax(£) | **Excluded** | Severe data scarcity originating across disjoint sources heavily escalates complex integration flaws. |
| engine (raw string) | **Excluded** | Key numeric magnitudes were extracted purposefully to construct isolated numerical categories. |

## **Derived attributes**

Given the diverse layouts characterizing the primary materials, A myriad of structured attributes were derived meticulously:

- **make (UK dataset):** The rudimentary UK file configurations contained brand names solely as file titles; therefore, systematic identification was utilized to inject brand descriptors into the dataset.
- **engineSize (Andrei Novikov dataset):** Within the Andrei Novikov grouping, specific numerical proportions specifying engine sizes were accurately parsed from complex string sequences utilizing sophisticated regular expressions.
- **mpg (Andrei Novikov dataset):** Disparate mpg ranges were condensed algebraically to construct a singular reliable mean.
- **model (Andrei Novikov dataset):** Car model names contained extra data and engine specifications, so the first word was isolated cleanly. 
- **make & model (Scraped EV dataset):** Mismatched model entries originally possessed brand names; consequently, the primary word was extracted programmatically to generate the make feature, while subsequent words were joined to accurately reconstruct the specific model.
- **age (All datasets):** A temporally sensitive age dimension was calculated explicitly by systematically subtracting the registered manufacturing year from each respective dataset's collection year (e.g., utilizing 2026 exclusively for the structurally scraped Autotrader entries).

## **Generated records**

No speculative or completely fabricated records were generated during the overarching synthesis of this study. However, The core structure was augmented extensively by folding in supplementary instances corresponding to Electric Vehicles retrieved newly from AutoTrader UK. Furthermore, Elaborate grouped imputation frameworks were deployed within the processing script to effectively address omissions and nulls. Hence, Missing categorical assignments were supplanted specifically utilizing local modes, while vacant continuous readings were successfully populated relying on grouped medians configured for matched make and model intersections. Ergo, Fundamental integrity was rigorously preserved whilst minimizing erroneous assumptions.

## **Merged data**

The independently synthesized data arrays were amalgamated uniformly through vertical concatenation into an all-encompassing unified design:

#### Feature renaming
Feature nomenclature was altered rigorously universally, whereby diverse column strings strictly mapped onto an identical nine-column standardized naming strategy.

#### Concatenation
The structures were executed uniformly, whereby international currencies alongside differing unit systems were translated successfully; specifically, the initial UK listings and modern AutoTrader captures were explicitly converted heavily into United States Dollars (USD) utilizing a strict 1.32 currency multiplication factor computationally, while imperial mpg scales were actively down-scaled to approximate standard American dimensions properly.

#### De-duplication
De-duplication algorithms were effectively implemented, dropping exact duplicate intersections systematically to fully preserve the integrity of the merged observations.

#### Null removal
This final purge was completed extensively to ensure no critical analytical voids remained within any categorical spheres. As a result, This singular architecture guarantees cohesive and structurally fluid datasets optimized for advanced machine manipulations.

## **Reformatted data**

According to the computational directives mapped, Heavy functional transformations were utilized to format varying structures harmoniously:

- **Consistent Casing:** Elaborate textual data points indicating classifications like structural models or transmission archetypes were normalized via whitespace eradication and universally standardized character string casing.
- **Standardised Category Labels:** String structures characterized by extreme categorical uniqueness were securely configured into official memory-efficient categorical data constraints.
- **Numerical Type Casting:** Continuous numerical dimensions were scaled downward specifically to 32-bit floating point implementations and concise numerical integers.
- **Column Ordering:** The datasets were systematically aligned to an identical array of eleven columns cleanly (`country`, `make`, `model`, `year`, `age`, `mileage`, `transmission`, `fuelType`, `mpg`, `engineSize`, `price`).
#### Export
Finally, The deliberate downsizing pipeline diminished the overarching memory consumption parameters significantly, demonstrating a heavily optimized computational framework overall. To conclude, The finalized CSV document furnishes a meticulously arranged asset ready for sophisticated algorithmic deployment.



## Ethical Considerations & Data Bias

In the context of the data evaluation, A prominent requirement was to formally address representational biases inherently tied to multi-sourced synthesis. Primarily, The uncoordinated temporal alignment between the historical Internal Combustion Engine (ICE) repositories and dynamically scraped AutoTrader Electric Vehicle (EV) registries introduces isolated inflation metrics and localized chronological volatility. Furthermore, Scraping real-time proprietary data specifically encapsulates acute geographical boundaries, consequently diminishing algorithmic applicability optimally across non-European markets. On the other hand, Methodologies systematically eradicated subjective vendor claims and isolated identifiers organically to rigorously enforce analytical objectivity. For the foreseeable future, Operating within these acknowledged constraints will significantly augment the transparency of overarching descriptive conclusions.

# Modelling

## Select Modelling Technique

During the initial evaluation phase, A myriad of numerical algorithms were deployed simultaneously to construct baseline market predictions:
- **Linear Regression:** Selected fundamentally to act as a simple baseline reference engineered unequivocally to reveal initial relationships between underlying features and ultimate pricing.
- **Ridge Regression:** Integrated actively because it manages correlated feature complexities (such as historically intertwined engine sizes and mpg figures) substantially better than standard linear constraints.
- **Lasso Regression:** Chosen explicitly owing to its programmatic ability to autonomously filter and isolate variables demonstrating the weakest valuation impact (such as country origins).
- **Decision Tree:** Implemented broadly to physically split structural properties, viewing distinct price variations cleanly across grouped characteristics (e.g., evaluating severe valuation gaps separating manual versus automatic architectures).
- **Random Forest:** Selected purposefully to stop stringent market outliers from routinely ruining regression accuracy, ensuring the final predictive pipeline uniformly produces stable output estimations.
- **Gradient Boosting:** Utilized to structurally learn exactly how isolated configurations influence valuation dynamically through sequential corrective steps, generating theoretically exceptional accuracy parameters.
- **K-Nearest Neighbors (KNN):** Deployed purely to cluster inventory possessing nearly identical metrics mathematically (notably isolating concurrent mileage tracking and fuel configurations), subsequently estimating pricing by directly averaging localized neighbors.
- **Champion Selection:** Following systemic testing, The Random Forest Regressor prominently differentiated itself and was conclusively assigned as the paramount predictive technique. 
- **Analytical Rationale:** Firstly, The Random Forest natively excels at managing highly non-linear depreciation trajectories and complex interacting automotive variables robustly. 
- **Deployment Efficiency:** Secondly, Deploying a Random Forest architecture into a generalized `.pkl` file is overwhelmingly smarter computationally. Unlike KNN—which structurally demands storing the entire expansive training dataset acting as inherent "parameters" to perpetually compute distance matrices during active inference—Random Forests exclusively record aggregated numerical threshold rules, exponentially diminishing the targeted memory footprint.

## Generate Test Design

To rigorously evaluate the predictive integrity of the algorithmic constructs, An expansive testing methodology was established explicitly:
- **Data Partitioning:** The entire dataset was partitioned strategically utilizing an 80/20 train-test split configuration. 
- **Training Sphere:** Precisely 544,555 randomized records were exclusively dedicated to the training sphere.
- **Evaluation Benchmark:** The terminating 136,139 instances were strictly isolated to function as an unseen systematic evaluation benchmark.
- **Validation Strategy:** To fortify the overarching validation, a strict 5-fold cross-validation strategy was implemented seamlessly. 
- **Feature Encoding:** Within this precise testing pipeline, Categorical structures characterized by low cardinality were systematically processed via One-Hot encoding, whereas high-cardinality descriptors (notably vehicle Make and Model strings) were transformed meticulously utilizing Binary Encoding to systematically prevent unwieldy memory matrix expansions.

## Build Model

The construction of the Random Forest framework involved elaborate hyperparameter optimization decisively targeting the maximization of empirical returns:
- **Sensitivity Analysis:** Initially, sensitivity analysis mapping the intrinsic constraints against assorted maximum algorithmic tree depths was rigorously executed. According to the generated readouts, deploying a targeted depth configuration of 20 optimally mitigated prominent overfitting risks while capturing expansive variance fluidly. 
- **Hyperparameter Tuning:** Subsequently, an exhaustive tuning pipeline was implemented systematically across exhaustive candidate configurations.
- **Definitive Formulation:** The structural configuration explicitly established configuring 300 sequential decision trees (`n_estimators`), parameterized seamlessly alongside a `max_depth` restrictively bound to 20, comprehensively operating across the entirety of accessible features (`max_features`: 1.0). In turn, these exact constraints systematically demolished algorithmic noise while actively reinforcing continuous price projections.

## Assess Model

According to the finalized empirical diagnostics, The meticulously tuned Random Forest architecture demonstrated mathematically exceptional financial estimations:
- **Mean Absolute Error (MAE):** The concluding tuned configuration recorded an MAE quantified at exactly $1,885.67, significantly outperforming the competing optimized KNN pipeline ($1,987.12).
- **Root Mean Squared Error (RMSE):** Parallelly, the architecture yielded a minimized RMSE amounting to $2,781.09.
- **Coefficient of Determination ($R^2$):** A phenomenal scoring benchmark was charted cleanly at 0.9492, verifying computationally that the infrastructure accurately encapsulates essentially 95% of the total variance associated with explicit pricing.
- **Mean Absolute Percentage Error (MAPE):** Furthermore, The algorithm generated an impressive MAPE of strictly 8.57%, definitively confirming that the constructed implementation delivers rigidly stabilized forecasting stability optimally.

# Evaluation

## Evaluate Results
- **Business Criteria Integrity:** The finalized structural pipeline generated a Mean Absolute Error (MAE) evaluated rigidly at $1,885.67 following hyperparameter optimization. Consequently, The model successfully traversed the stringent $2,000 algorithmic threshold fundamentally mandated to support viable buyer/seller deployment decisions.
- **Technical Benchmarks:** Analyzing the overarching computational metrics, All seven independent machine learning algorithms successfully exceeded the strictly isolated $R^2$ baseline limit (0.80). Furthermore, The champion Random Forest configuration autonomously achieved an elite 0.9492 reading following tuning.

## Review Process
- **Data Architecture Validation:** All relevant repositories (encompassing historical ICE datasets and dynamically scraped AutoTrader EV groupings) were ingested successfully. Furthermore, Strict 80/20 train-test evaluation splits were maintained seamlessly without introducing systemic data leakages.
- **Encoding Transitions:** A myriad of numerical architectures were interrogated rigorously. Consequently, transitioning from baseline encoders to formalized Binary Encoding transformations successfully mitigated explosive system-level memory expansion constraints natively.
- **Fairness & Subjectivity:** Formal ethical metrics systematically guarantee that absolutely zero personally identifiable vectors were utilized during inference. However, Regional financial bias traversing the UK and US models intrinsically necessitated the deployment of live FX exchange correctives.

## Determine Next Steps
- **Data Scarcity Mitigations:** Since legacy historical matrices intrinsically lacked Electric Vehicle (EV) parity, The procedural pipeline successfully advanced into utilizing persistent web automation scripts (Playwright) securely to eradicate valuation shortcomings.
- **Systemic Expansion:** For the foreseeable future, Expanding localized datasets natively requires deploying autonomous web scrapers systematically, actively circumventing manual CSV dependency.

# Deployment

## Deployment Architecture
- **Backend Application Programming Interface (API):** The infrastructure centers on a highly resilient FastAPI REST architecture, natively supplying a dynamic `/predict` inference endpoint to external consumers.
- **Frontend Dashboard Engine:** An aggressive dark-themed Streamlit web interface was implemented strictly to empower direct consumer interaction while seamlessly managing intricate feature formatting internally.
- **Continuous Ingestion Mechanics:** A localized Playwright-driven Python scraper (`scraper.py`) securely executes automated interrogations against AutoTrader UK, continuously expanding the available algorithmic EV baseline.

## Integration Strategy
- **Algorithmic Serialization:** The highly optimized Random Forest pipeline alongside corresponding encoding rules was decisively compiled into a standard `joblib` `.pkl` manifest for rapid memory activation.
- **Dynamic FX Normalization:** The overarching FastAPI construct natively queries live currency exchange APIs (USD/GBP) at inference time. Ergo, Real-world economic circumstances strictly override embedded historical pricing static constants.
- **Fallback Imputation Tactics:** Standardized Internal Combustion Engine (ICE) medians (such as assuming 45.0 mpg efficiencies and 1.6L engine profiles) are intentionally injected into requested EV matrices manually to completely adhere to trained dimensional structures.

## Operations & Monitoring
- **Performance Evaluation Systems:** Output precision validations natively require the monthly recalculation of structural MAE and $R^2$ scores tracking cleanly against evolving public market records.
- **Data Drift Identification:** Standard bi-weekly evaluations aggressively target missing-value thresholds manifesting directly within the newly scraped operational inputs.
- **Automated Retraining Protocols:** Scheduled automated retraining protocols are designed exclusively to initialize sequentially following significant acquisitions of modernized web data.