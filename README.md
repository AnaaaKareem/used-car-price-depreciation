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
