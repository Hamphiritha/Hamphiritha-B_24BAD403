Introduction to Python Libraries and Dataset Preprocessing 


SCENARIO 1: E-Commerce Sales Data

Objective
Analyze product sales trends and detect missing information in an e-commerce dataset.

Steps Performed
•	Imported Pandas, NumPy, and Matplotlib
•	Loaded dataset into a Pandas DataFrame
•	Inspected data using head(), tail(), info(), and describe()
•	Checked missing values using isnull().sum()
•	Calculated total sales using Quantity × UnitPrice
•	Visualized top products using:
o	Bar chart
o	Line chart

Observations
•	Missing values were found in the Description and CustomerID columns
•	Some products generated significantly higher revenue than others
•	Sales distribution was highly skewed with few top-selling products



SCENARIO 2: Hospital Patient Records

Objective
Identify missing health metrics and analyze patient health patterns.

Steps Performed
•	Loaded dataset into Pandas
•	Explored structure and missing values
•	Identified zero values in medical attributes
•	Replaced zero values with NaN
•	Visualized:
o	Glucose levels using histogram
o	Age distribution using boxplot
•	Analyzed mean health metrics grouped by outcome

Observations
•	Zero values were present in Glucose, BloodPressure, BMI, Insulin
•	Patients with diabetes showed:
o	Higher glucose levels
o	Higher BMI on average
•	Age distribution showed wider spread among diabetic patients



SCENARIO 3: Housing Dataset

Objective
Examine missing housing features and relationships affecting house prices.

Steps Performed
•	Loaded housing dataset
•	Inspected column types and missing values
•	Visualized relationships using:
o	Scatter plots
o	Correlation heatmaps

Observations
•	Missing values observed in features such as lot size and bedrooms
•	Strong correlation found between:
o	House size and price
o	Number of rooms and price
•	Visualization helped clearly identify predictors for price estimation



SCENARIO 4: Banking Customer Data

Objective
Understand customer demographics and detect missing banking information.

Steps Performed
•	Imported dataset into Pandas
•	Examined data structure and null values
•	Visualized:
o	Age distribution (bar plot)
o	Income distribution (box plot)
o	Spending behavior

Observations
•	Missing values found in Income and Customer profile fields
•	Middle-aged customers showed higher spending
•	Higher income customers tended to spend more on premium products
 








