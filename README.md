# citibike-data-engineering
## Overiew
This project designs and implements a PostgreSQL database to store and analyse 2016 Citi Bike trip data alongside corresponding weather Newark Airport. The database will also include complex SQL views to support data analytic investigations.

## Objectives
- Create a normalised postgreSQL database schema that integrates Citi Bike trip data and Newark Airport data.
- Develop a robust Extract Tranform and Load (ETL) pipeline to load CSV data into relational tables.
- Construct SQL views that generate insights for data analytic queries and reporting.

## Background
This project was inspired  by a Codecademy portfolio task that focused on improving data engineering skills. The project outline is located here: [Codecademy](https://www.codecademy.com/paths/data-engineer/tracks/decp-data-management-portfolio-project/modules/decp-data-management-portfolio-project/kanban_projects/bike-rental-data-management-portfolio-project).
The purpose of this project is to demonstrate my data engineering skills in schema design, database normalisation, ETL development and analytical engineering.

## Prequisites
### Data Sources
- citibike-tripdata.csv [per month in 2016]
- newark_airport_2016.csv

### Tools and Platforms
- Exploratory Data Analysis: Jupyter Notebook (Python)
- Database Schema Design: Lucidchart
- Database Platform: PostgreSQL
- ETL Scripting: Python
- Version Control and Automation: GitHub and GitHub Actions

## Procedure
### 1. data-preparation
- Create GitHub branches for each major workflow component.
- Review the data and the data dictionaries: citibike.pdf and weather.pdf.
- Perform an exploratory data analysis (EDA) to detect data issues.

### 2. design-schema
- Define the list of required tables and fields.
- Assign appropriate data types and relationships.
- Normalise the schema, refer to: [Appfarm](https://docs.appfarm.io/appcademy/background/databases/database-normalization).

### 3. create-database
- Create the PostgreSQL database.
- Create all tables referring to the schema.
- Add constraints and indexes to each table.

### 4. design-etl
- Design the etl process based on the EDA results.
- Write a python-based ETL script.
- Validate row counts, formats and integrity post-load.

### 5. create-views
- Design and test views that support analytics and reporting.
- Verify view outputs using sample queries.

### 6. production
- Finalise the README file.s
- Complete any outstanding tasks or issues.

## Project Results

### Exploratory Data Analysis Summary
#### Detected Duplicate Values

#### Detected Missing Values

### Schema Design Notes

### Database Creation Results

### ETL Pipeline Results

## References
[Appfarm] -  https://docs.appfarm.io/appcademy/background/databases/database-normalization


