# Task 8 & Task 9 - ETL Pipeline and Analytical Views

## Overview

Tasks 8 and 9 complete the Citi Bike data engineering pipeline by loading data into PostgreSQL and creating comprehensive analytical views using the **dataflow-pro** library.

---

## Task 8: ETL Pipeline

### Purpose
Load transformed data into PostgreSQL tables in the correct order (dimensions first, then facts) with comprehensive monitoring, validation, and error handling.

### Key Features

#### 1. **Pipeline Configuration**
Uses `dataflow_pro.pipeline.PipelineConfig` to configure:
- Pipeline name: `citibike_etl_pipeline`
- Pipeline type: `BATCH`
- Schema model: `STAR`
- Parallel processing: Enabled
- Memory limit: 4GB
- Monitoring: Enabled
- Target connection: PostgreSQL connection string
- Business objectives: Daily trip analysis, weather impact, station popularity, user demographics, temporal patterns

#### 2. **Pipeline Monitoring**
Uses `dataflow_pro.pipeline.create_monitoring_pipeline` to track:
- Quality monitoring
- Performance monitoring
- Resource monitoring
- Execution ID tracking
- Stage-by-stage metrics

#### 3. **Pre-ETL Validation**
- Re-validates all transformed datasets against business rules
- Uses `RuleValidator` from dataflow-pro
- Generates detailed violation logs
- Captures quality scores before loading

#### 4. **Batch Loading**
- Loads tables in dependency order: `Users`, `Bike_Stations`, `Weather_Stations`, `Weather_Dates`, `Trips`
- Batch size: 10,000 records per batch
- Uses SQLAlchemy with `to_sql()` method
- Progress tracking every 10 batches
- Database verification after each table load

#### 5. **Comprehensive Reporting**
Generates two detailed logs:

**Violation Log** (`etl_validation_violations_*.log`):
- Overall validation summary
- Failed rules by table
- Sample violations
- Violation counts

**ETL Pipeline Report** (`etl_pipeline_report_*.log`):
- Pipeline configuration
- Pre-ETL validation summary
- Load results by table (records loaded, duration, throughput)
- Overall ETL summary
- Monitoring metrics

### Load Order
```python
load_order = ['Users', 'Bike_Stations', 'Weather_Stations', 'Weather_Dates', 'Trips']
```

This ensures:
1. Dimension tables loaded first
2. Fact tables loaded last (after foreign key dependencies exist)

### Error Handling
- Try-catch blocks around each table load
- Failed batches are logged
- Partial failures tracked
- Status reporting: SUCCESS, PARTIAL, or FAILED

### Output Metrics
- Total tables loaded
- Total records loaded
- Success rate percentage
- Duration and throughput (records/sec)
- Quality score from validation

---

## Task 9: Create Analytical Views

### Purpose
Generate comprehensive SQL views that join all tables in the star schema for analytical queries, using relationships detected in Task 5.

### Key Features

#### 1. **SQL Generator Initialization**
Uses `dataflow_pro.pipeline.SQLGenerator`:
- Target database: PostgreSQL
- Schema model: Star schema

#### 2. **Business Objectives**
Defines analytical requirements:
- Comprehensive trip analysis
- Daily trip summary
- Station popularity
- User demographics
- Weather impact
- Temporal patterns

#### 3. **Comprehensive View (vw_trip_analysis)**

**Tables Joined:**
- `Trips` (fact table - main anchor)
- `Users` (dimension)
- `Bike_Stations` (dimension - used twice for start/end stations)
- `Weather_Dates` (fact table - temporal join)
- `Weather_Stations` (dimension)

**Join Strategy:**
```sql
FROM "Trips" t
INNER JOIN "Users" u ON t."User ID" = u."User ID"
INNER JOIN "Bike_Stations" ss ON t."Start Station ID" = ss."Station ID"
INNER JOIN "Bike_Stations" es ON t."End Station ID" = es."Station ID"
LEFT JOIN "Weather_Dates" wd ON t."Start Date" = wd."DATE"
LEFT JOIN "Weather_Stations" ws ON wd."Weather Station ID" = ws."Weather Station ID"
```

**Columns Included:**
- All trip data (prefixed with `trip_`)
- All user data (prefixed with `user_`)
- Start station data (prefixed with `start_station_`)
- End station data (prefixed with `end_station_`)
- Weather data (prefixed with `weather_`)
- Weather station data (prefixed with `weather_station_`)

**Derived Metrics:**
- Temporal: `trip_year`, `trip_month`, `trip_day`, `trip_hour`, `trip_day_of_week`, `trip_day_name`, `trip_month_name`
- Duration: `trip_duration_minutes`, `trip_duration_category`
- User: `user_age_at_trip`, `user_gender_label`
- Trip classification: `trip_day_type` (Weekday/Weekend), `trip_time_category` (Morning Peak, Midday, Evening Peak, Night)
- Weather: `temperature_category`, `precipitation_category`, `weather_avg_temp_celsius`
- Distance: `trip_distance_km` (Haversine formula)

**Performance Indexes:**
```sql
CREATE INDEX idx_vw_trip_analysis_date ON "Trips"("Start Date");
CREATE INDEX idx_vw_trip_analysis_start_station ON "Trips"("Start Station ID");
CREATE INDEX idx_vw_trip_analysis_end_station ON "Trips"("End Station ID");
CREATE INDEX idx_vw_trip_analysis_user ON "Trips"("User ID");
CREATE INDEX idx_weather_dates_lookup ON "Weather_Dates"("DATE");
```

#### 4. **Summary Views**

**vw_daily_trip_summary:**
- Aggregates trips by date
- Metrics: total trips, unique bikes, unique users, average duration/distance, subscriber vs customer split, weather averages

**vw_station_popularity:**
- Station-level metrics
- Metrics: total departures, active days, average trip duration, unique users
- Ordered by total departures

**vw_user_demographics_summary:**
- User segmentation analysis
- Dimensions: user type, gender, age group
- Metrics: total trips, average duration/distance
- Age groups: Under 20, 20-29, 30-39, 40-49, 50-59, 60+

**vw_weather_impact_summary:**
- Weather impact on ridership
- Dimensions: temperature category, precipitation category, day type
- Metrics: total trips, average duration/distance, unique users

**vw_hourly_peak_analysis:**
- Hourly patterns
- Dimensions: hour, time category, day type
- Metrics: total trips, average duration, unique stations

**vw_monthly_trends:**
- Monthly aggregations
- Metrics: total trips, averages, subscriber/customer split
- Ordered by year and month

#### 5. **View Creation Process**

1. **Generate SQL:** Build comprehensive view and summary views
2. **Save to File:** Write to `sql/02_create_analytical_views.sql`
3. **Execute in Database:** Create all views in PostgreSQL
4. **Grant Permissions:** Grant SELECT to PUBLIC for all views
5. **Verify Creation:** Query `information_schema.views` to confirm
6. **Row Count Check:** Count rows in each view to validate data

### Output Files
- `sql/02_create_analytical_views.sql` - Complete SQL script with all view definitions

### Views Created
1. `vw_trip_analysis` - Comprehensive analytical view
2. `vw_daily_trip_summary` - Daily aggregations
3. `vw_station_popularity` - Station metrics
4. `vw_user_demographics_summary` - User analysis
5. `vw_weather_impact_summary` - Weather correlations
6. `vw_hourly_peak_analysis` - Temporal patterns
7. `vw_monthly_trends` - Monthly statistics

---

## Usage Examples

### Query Comprehensive Trip Data
```sql
SELECT * FROM vw_trip_analysis
WHERE trip_start_date = '2016-07-04'
LIMIT 100;
```

### Analyze Daily Patterns
```sql
SELECT
    trip_start_date,
    trip_day_name,
    total_trips,
    avg_temperature,
    avg_precipitation
FROM vw_daily_trip_summary
ORDER BY trip_start_date;
```

### Find Most Popular Stations
```sql
SELECT
    start_station_station_name,
    total_departures,
    active_days,
    avg_trip_duration_minutes
FROM vw_station_popularity
ORDER BY total_departures DESC
LIMIT 20;
```

### Weather Impact Analysis
```sql
SELECT
    temperature_category,
    precipitation_category,
    trip_day_type,
    total_trips,
    avg_duration_minutes
FROM vw_weather_impact_summary
ORDER BY total_trips DESC;
```

### User Demographics
```sql
SELECT
    user_user_type,
    age_group,
    user_gender_label,
    total_trips,
    avg_distance_km
FROM vw_user_demographics_summary
ORDER BY total_trips DESC;
```

---

## How to Run

### Prerequisites
1. Database connection configured in `.env`
2. All dimension and fact tables created (Task 7)
3. Schema relationships defined (Task 5)
4. Business rules defined (Task 3)

### Execute Tasks

**Task 8 - ETL Pipeline:**
```python
# Run cell 22 in the Jupyter notebook
# This will:
# 1. Configure pipeline
# 2. Validate data
# 3. Load all tables to PostgreSQL
# 4. Generate comprehensive reports
```

**Task 9 - Create Views:**
```python
# Run cell 24 in the Jupyter notebook
# This will:
# 1. Generate view SQL
# 2. Create views in database
# 3. Verify creation
```

### Expected Results

**Task 8 Output:**
- ✓ 5 tables loaded successfully
- ✓ ~270,000+ trip records loaded
- ✓ Validation quality score displayed
- ✓ Two log files generated in `logs/` directory

**Task 9 Output:**
- ✓ 7 analytical views created
- ✓ SQL file saved to `sql/02_create_analytical_views.sql`
- ✓ Row counts displayed for each view
- ✓ Usage examples printed

---

## Dependencies

**dataflow-pro Modules Used:**

Task 8:
- `dataflow_pro.pipeline.PipelineConfig`
- `dataflow_pro.pipeline.create_monitoring_pipeline`
- `dataflow_pro.rules.RuleValidator`

Task 9:
- `dataflow_pro.pipeline.SQLGenerator`
- `dataflow_pro.pipeline.DatabaseDialect`
- `dataflow_pro.pipeline.SchemaModel`

**Other Libraries:**
- `sqlalchemy` - Database operations
- `psycopg[binary]` - PostgreSQL driver (psycopg3)
- `pandas` - DataFrame operations
- `pathlib` - File path handling
- `datetime`, `uuid` - Timestamps and IDs

---

## Monitoring and Logging

### Execution Tracking
- Unique execution ID generated for each run
- Start/end times tracked
- Performance metrics captured per stage
- Resource usage monitored

### Quality Metrics
- Pre-ETL validation quality score
- Rule compliance percentage
- Violation counts by table
- Sample violations logged

### Performance Metrics
- Records loaded per table
- Duration per table (seconds)
- Throughput (records/second)
- Overall pipeline duration
- Success/failure rates

---

## Troubleshooting

### Common Issues

**Connection Errors:**
- Verify PostgreSQL is running
- Check `.env` configuration
- Ensure database exists
- Verify connection string uses `postgresql+psycopg://`

**Table Not Found:**
- Ensure Task 7 (SQL table creation) completed successfully
- Verify tables exist: `SELECT * FROM information_schema.tables WHERE table_schema = 'public'`

**Foreign Key Violations:**
- Check load order (dimensions before facts)
- Verify data integrity in source DataFrames

**View Creation Errors:**
- Check column names match between tables
- Verify all tables exist before creating views
- Review SQL syntax in generated file

**Performance Issues:**
- Adjust batch size (default: 10,000)
- Enable parallel processing
- Create indexes before loading large datasets
- Monitor memory usage (limit: 4GB)

---

## Best Practices

1. **Always validate before loading:** Task 8 runs validation to catch issues early
2. **Monitor progress:** Check logs during long-running loads
3. **Verify after loading:** Compare loaded counts with source data
4. **Review violation logs:** Understand data quality issues
5. **Test views incrementally:** Query each view after creation
6. **Backup before re-running:** ETL uses `if_exists='append'`, may duplicate data
7. **Check indexes:** Ensure indexes exist for optimal query performance

---

## Generated Reports Location

```
citibike-data-engineering/
├── logs/
│   ├── etl_validation_violations_YYYYMMDD_HHMMSS.log
│   └── etl_pipeline_report_YYYYMMDD_HHMMSS.txt
└── sql/
    └── 02_create_analytical_views.sql
```

---

## Summary

**Task 8** loads ~270,000+ trip records across 5 tables into PostgreSQL with full validation, monitoring, and error handling, generating comprehensive execution reports.

**Task 9** creates 7 analytical views that join all tables together, providing pre-built queries for trip analysis, user demographics, station popularity, weather impact, and temporal patterns.

Together, these tasks complete the ETL pipeline and make the data ready for business intelligence and analytical queries.
