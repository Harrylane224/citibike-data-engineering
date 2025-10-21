# Citi Bike Data Engineering Project 🚴‍♂️

## Project Overview

This project demonstrates a comprehensive data engineering solution that integrates 2016 Citi Bike trip data with Newark Airport weather data into a normalised PostgreSQL database. The solution includes data quality assessment, business rule validation, ETL pipeline design, and analytical view creation.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Project Tasks](#project-tasks)
- [Database Schema](#database-schema)
- [Usage](#usage)
- [Reports and Outputs](#reports-and-outputs)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)

## Project Structure

```
citibike-data-engineering/
├── data-sources/
│   └── data/
│       ├── JC-201601-citibike-tripdata.csv
│       ├── JC-201602-citibike-tripdata.csv
│       ├── ... (12 monthly files)
│       └── newark_airport_2016.csv
├── reports/
│   ├── citibike_data_quality_assessment.html
│   ├── citibike_rule_validation_assessment.html
│   ├── citibike_star_schema_design_report.html
│   └── citibike_star_schema_er_diagram.png
├── sql/
│   ├── 01_create_star_schema.sql
│   └── 02_create_analytical_views.sql
├── logs/
│   ├── etl_validation_violations_*.log
│   └── etl_pipeline_report_*.txt
├── .env
├── requirements.txt
├── citibike_project.ipynb
└── README.md
```

## Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Jupyter Notebook or JupyterLab

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd citibike-data-engineering
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   ```sql
   CREATE DATABASE citibike_db;
   ```

5. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=citibike_db
   DB_USER=postgres
   DB_PASSWORD=your_password_here
   ```

## Data Sources

### Citi Bike Trip Data
- **Period**: January - December 2016
- **Location**: Jersey City, New Jersey
- **Files**: 12 monthly CSV files
- **Records**: ~270,000+ trips
- **Attributes**: Trip duration, start/stop times, station information, user type, demographics

### Weather Data
- **Source**: Newark Airport Weather Station
- **Period**: Full year 2016
- **Metrics**: Temperature, precipitation, snow, wind speed
- **Temporal Granularity**: Daily measurements

## Project Tasks

### Task 1: Data Preparation
- Loaded 12 monthly Citi Bike CSV files using dataflow-pro's DataLoader
- Loaded Newark Airport weather data
- Handled schema inconsistencies across monthly files
- Used PyArrow for efficient data processing

### Task 2: Data Quality Assessment
- Conducted comprehensive quality analysis on raw datasets
- Generated detailed HTML assessment report
- Identified data quality issues across:
  - Null values
  - Data type inconsistencies
  - Outliers and anomalies
  - Duplicate records
- Calculated overall quality scores for each dataset

### Task 3: Business Rule Validation
- Created 8 custom business rules based on data dictionary:
  - Datetime range validation (2016 boundaries)
  - Geographic coordinate validation (NJ region)
  - Categorical value validation (user types, gender codes)
  - Numeric range validation (birth years, latitude/longitude)
- Generated validation reports with violation counts
- Created detailed violation logs for non-compliant records

### Task 4: Data Transformation
- Designed star schema with normalised tables:
  - **Dimension Tables**: Users, Bike_Stations, Weather_Stations
  - **Fact Tables**: Trips, Weather_Dates
- Extracted unique dimension records from raw data
- Created surrogate keys where needed
- Established foreign key relationships
- Added derived columns (e.g., Start Date for temporal joins)

### Task 5: Schema Design
- Used dataflow-pro's schema module for relationship detection
- Auto-detected foreign key relationships between tables
- Manually added temporal join (Trips → Weather_Dates)
- Generated entity-relationship (ER) diagram
- Produced comprehensive schema design report

### Task 6: Create SQL Tables
- Generated PostgreSQL DDL using schema design output
- Defined primary keys and foreign key constraints
- Added strategic indexes for query optimisation
- Documented table structures and relationships

### Task 7: Execute SQL Tables
- Connected to PostgreSQL database using SQLAlchemy
- Executed DDL to create all star schema tables
- Verified table creation with metadata inspection
- Confirmed primary keys, foreign keys, and indexes

### Task 8: Design ETL Pipelines
- Built comprehensive ETL pipeline using dataflow-pro
- Implemented batch processing (10,000 records per batch)
- Added data validation during ETL process
- Created detailed violation logs for rule failures
- Loaded data in correct order (dimensions → facts)
- Generated ETL execution report with metrics:
  - Records loaded per table
  - Processing throughput (records/second)
  - Success/failure rates
  - Duration and performance statistics

### Task 9: Create SQL Views
- Created comprehensive analytical view (vw_trip_analysis) joining all tables
- Added derived metrics:
  - Trip distance calculations (Haversine formula)
  - User age at time of trip
  - Temporal categorisations (peak hours, weekday/weekend)
  - Weather categorisations (temperature bands, precipitation levels)
- Built 4 additional summary views:
  - Daily trip summary
  - Station popularity metrics
  - User demographics analysis
  - Weather impact on ridership
- Optimised views with strategic indexes

## Database Schema

### Star Schema Design

**Dimension Tables:**

1. **Users**
   - Primary Key: User ID
   - Attributes: User Type, Birth Year, Gender

2. **Bike_Stations**
   - Primary Key: Station ID
   - Attributes: Station Name, Latitude, Longitude

3. **Weather_Stations**
   - Primary Key: Weather Station ID
   - Attributes: Station Code, Name

**Fact Tables:**

1. **Trips**
   - Foreign Keys: User ID, Start Station ID, End Station ID
   - Measures: Trip Duration, Start Time, Stop Time, Start Date, Bike ID

2. **Weather_Dates**
   - Foreign Key: Weather Station ID
   - Measures: DATE, PRCP, SNOW, SNWD, TMAX, TMIN, AWND

**Analytical Views:**

- `vw_trip_analysis`: Comprehensive view joining all tables with derived metrics
- `vw_daily_trip_summary`: Daily aggregations and statistics
- `vw_station_popularity`: Station usage metrics
- `vw_user_demographics_summary`: User demographic analysis
- `vw_weather_impact_summary`: Weather impact on ridership

## Usage

### Running the Jupyter Notebook

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook citibike_project.ipynb
   ```

2. **Execute cells sequentially** from Task 1 through Task 9

3. **Review generated reports** in the `reports/` directory

### Querying the Database

```sql
-- Example 1: Get comprehensive trip data
SELECT * FROM vw_trip_analysis
WHERE trip_date = '2016-07-04'
LIMIT 100;

-- Example 2: Analyse daily patterns
SELECT
    trip_date,
    trip_day_name,
    total_trips,
    avg_temperature,
    avg_precipitation
FROM vw_daily_trip_summary
ORDER BY trip_date;

-- Example 3: Find most popular stations
SELECT
    station_name,
    total_departures,
    active_days,
    avg_trip_duration / 60.0 as avg_duration_minutes
FROM vw_station_popularity
ORDER BY total_departures DESC
LIMIT 20;

-- Example 4: Weather impact analysis
SELECT
    temperature_category,
    precipitation_category,
    trip_day_type,
    total_trips,
    avg_duration_seconds / 60.0 as avg_duration_minutes
FROM vw_weather_impact_summary
ORDER BY total_trips DESC;

-- Example 5: User demographics
SELECT
    user_type,
    age_group,
    user_gender_label,
    total_trips,
    ROUND(avg_distance_km, 2) as avg_distance_km
FROM vw_user_demographics_summary
ORDER BY total_trips DESC;
```

## Reports and Outputs

### HTML Reports
1. **Data Quality Assessment** (`citibike_data_quality_assessment.html`)
   - Comprehensive quality metrics for each dataset
   - Statistical summaries and distributions
   - Data type analysis
   - Null value detection
   - Outlier identification

2. **Rule Validation Assessment** (`citibike_rule_validation_assessment.html`)
   - Business rule compliance results
   - Violation counts and percentages
   - Rule-by-rule breakdown
   - Severity classifications

3. **Schema Design Report** (`citibike_star_schema_design_report.html`)
   - Executive summary
   - Table structure documentation
   - Relationship analysis
   - Confidence scores
   - Deployment guidance

### Diagrams
- **ER Diagram** (`citibike_star_schema_er_diagram.png`)
  - Visual representation of star schema
  - Table relationships
  - Primary and foreign keys

### SQL Scripts
1. **Table Creation** (`01_create_star_schema.sql`)
   - DDL for all dimension and fact tables
   - Primary key definitions
   - Foreign key constraints
   - Index creation

2. **View Creation** (`02_create_analytical_views.sql`)
   - Comprehensive analytical view
   - Summary views for common analyses
   - Optimisation indexes

### Log Files
1. **Validation Violations** (`etl_validation_violations_*.log`)
   - Detailed record of all business rule violations
   - Organised by table and rule type
   - Severity levels and counts

2. **ETL Pipeline Report** (`etl_pipeline_report_*.txt`)
   - Load statistics per table
   - Processing throughput metrics
   - Success/failure rates
   - Overall pipeline summary

## Technologies Used

### Data Processing
- **Pandas**: Data manipulation and analysis
- **Polars**: High-performance DataFrame operations
- **PyArrow**: Columnar data format and efficient processing
- **DuckDB**: In-memory analytical database

### Database
- **PostgreSQL**: Production relational database
- **SQLAlchemy**: Python SQL toolkit and ORM
- **psycopg**: PostgreSQL adapter for Python

### Data Engineering Framework
- **dataflow-pro**: Custom data engineering framework featuring:
  - Data quality assessment
  - Schema design and relationship detection
  - Business rule validation
  - ETL pipeline orchestration
  - Report generation

### Visualisation
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualisation
- **Plotly**: Interactive charts

### Development
- **Jupyter Notebook**: Interactive development environment
- **python-dotenv**: Environment variable management
- **tqdm**: Progress bars for long-running operations

## Key Features

### Data Quality
- ✅ Comprehensive quality assessment with scoring
- ✅ Automated issue detection and classification
- ✅ HTML report generation with visualisations

### Business Rules
- ✅ Customisable rule definitions
- ✅ Multiple severity levels (error, warning, info)
- ✅ Detailed violation logging
- ✅ Rule-based data validation during ETL

### Schema Design
- ✅ Automatic relationship detection
- ✅ Star schema optimisation
- ✅ Foreign key constraint enforcement
- ✅ Index strategy for query performance

### ETL Pipeline
- ✅ Batch processing for large datasets
- ✅ Parallel processing support
- ✅ Error handling and recovery
- ✅ Comprehensive logging and monitoring
- ✅ Data validation integration

### Analytics
- ✅ Pre-built analytical views
- ✅ Derived metrics and categorisations
- ✅ Temporal analysis capabilities
- ✅ Weather correlation analysis
- ✅ User behaviour insights

## Business Value

This solution enables comprehensive analysis of bike-sharing patterns, including:

- **User Behaviour**: Understanding customer vs. subscriber patterns, demographics, and usage trends
- **Operational Insights**: Station demand analysis, bike utilisation, peak hour identification
- **Weather Impact**: Correlation between weather conditions and ridership
- **Temporal Trends**: Hourly, daily, weekly, and seasonal patterns
- **Geographic Analysis**: Station popularity, route analysis, service area coverage

The normalised star schema design optimises query performance for analytical workloads while maintaining data integrity through proper constraints and relationships.

## Future Enhancements

Potential areas for expansion:

- [ ] Real-time data streaming pipeline
- [ ] Machine learning models for demand forecasting
- [ ] Interactive dashboards using Tableau/Power BI
- [ ] Geospatial analysis with PostGIS
- [ ] API development for data access
- [ ] Data warehouse integration
- [ ] Advanced anomaly detection

## Project Status

✅ **COMPLETE**

All tasks successfully implemented with comprehensive documentation, testing, and validation. The database is production-ready for analytical queries and business intelligence applications.

## Author

Data Engineering Project - 2025

## Acknowledgements

- Citi Bike for providing open trip data
- NOAA for weather data
- dataflow-pro framework developers

---

**Note**: This project uses Australian English spelling conventions (e.g., "organisation" instead of "organization") as per the developer's preference.