# **Citi Bike Data Engineering  - Exploratory Data Analysis**

## Purpose
The primary objective of the Exploratory Data Analysis (EDA) is to examine the structure, quality and characteristics of each raw dataset before designing the database schema. This approach will also provide insights into the shape and semantics of the data, leading to a more efficient, normalised and error-tolerant schema. By proactively outlining these data quality issues, the EDA will help mitigate future complications in downstream ETL processes and workflows, while also establishing  saves time and maintains record-keeping that could impact downstream processing and analytics.

## Prequisites
### Data Sources
The following are the names of each CSV file and provides their location:
- [newark_airport_2016.csv](../data-sources/data/newark_airport_2016.csv)
- [JC-201601-citibike-tripdata.csv](../data-sources/data/JC-201601-citibike-tripdata.csv)
- [JC-201602-citibike-tripdata.csv](../data-sources/data/JC-201602-citibike-tripdata.csv)
- [JC-201603-citibike-tripdata.csv](../data-sources/data/JC-201603-citibike-tripdata.csv)
- [JC-201604-citibike-tripdata.csv](../data-sources/data/JC-201604-citibike-tripdata.csv)
- [JC-201605-citibike-tripdata.csv](../data-sources/data/JC-201605-citibike-tripdata.csv)
- [JC-201606-citibike-tripdata.csv](../data-sources/data/JC-201606-citibike-tripdata.csv)
- [JC-201607-citibike-tripdata.csv](../data-sources/data/JC-201607-citibike-tripdata.csv)
- [JC-201608-citibike-tripdata.csv](../data-sources/data/JC-201608-citibike-tripdata.csv)
- [JC-201609-citibike-tripdata.csv](../data-sources/data/JC-201609-citibike-tripdata.csv)
- [JC-201610-citibike-tripdata.csv](../data-sources/data/JC-201610-citibike-tripdata.csv)
- [JC-201611-citibike-tripdata.csv](../data-sources/data/JC-201611-citibike-tripdata.csv)
- [JC-201612-citibike-tripdata.csv](../data-sources/data/JC-201612-citibike-tripdata.csv)

### Reference Material
 The following are the names and links of each **Data Dictionary**:
- [citibike.pdf](../data-sources/data-dictionaries/citibike.pdf)
- [weather.pdf](../data-sources/data-dictionaries/weather.pdf)

### Analytical Environment
#### Virtual Environment
Version: Python 3.9
Virtual Environment: venv
#### Packages
(installed via requirements.txt)

## Key Components of EDA
### 1. Data Structure Inspection
The notebook is located here: [1_data_structure_inspection.ipynb](notebooks/1_data_structure_inspection.ipynb)
- Evaluate consistency with provided data dictionaries.
- Create lists of column names, data types and inferred domains (distinct, valid and expected values).
- Detect column groupings for entity relationships.


### 2. Duplicate Detection
The notebook is located here: [2_duplicate_detection.ipynb](notebooks/2_duplicate_detection.ipynb)
- Assess whether duplicate rows exist in the dataset.
- Determine uniqueness of identifiers (e.g. primary keys).

### 3. Missing Values Analysis
The notebook is located here: [3_missing_values.ipynb](notebooks/3_missing_values.ipynb)
- Identify and quantify the number of missing values in relevant columns.
- Spot and confirm the data missing patterns (e.g. MAR, MCAR, etc).

### 4. Outlier and Range Validation
- Outline Business Logic Constraints
- Detect Categorical and Quantitative Outliers

### 5. Value Distributions
- Identify low-caridinality columns for dimension tables.
- Spot potential data normalisation opportunities.

### 6. Relationship Inference
- Evaluate if certain fields to form foreign key relationships.

### 7. Data Volume Estimation
- Recording row counts and file sizes to assist with testing of downstream builds.

### 8. Unit and Format Consistency
- Validate uniform measurement units.
- Confirm formatting standards for fields like dates, times, numbers.

## Expected Outcomes
Once the EDA has been completed, the following information will be populated in [eda_insights](eda_insights.md):
- Tables and Definitions
- Fields(columns), data types and constraints
- Primary Keys/Foreign Keys
- Indexing Strategies