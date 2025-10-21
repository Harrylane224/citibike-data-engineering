-- Citi Bike Star Schema - PostgreSQL DDL
-- Generated: 2025-10-20 23:06:13

-- Create Tables First
CREATE TABLE "Users" (
    "User ID" SMALLINT NOT NULL,
    "User Type" TEXT NOT NULL,
    "Birth Year" REAL NOT NULL,
    "Gender" SMALLINT NOT NULL,
    PRIMARY KEY ("User ID")
);

CREATE TABLE "Bike_Stations" (
    "Station ID" SMALLINT NOT NULL,
    "Station Name" TEXT NOT NULL,
    "Latitude" REAL NOT NULL,
    "Longitude" REAL NOT NULL,
    PRIMARY KEY ("Station ID")
);

CREATE TABLE "Weather_Stations" (
    "Weather Station ID" SMALLINT NOT NULL,
    "Station" TEXT NOT NULL,
    "Name" TEXT NOT NULL,
    PRIMARY KEY ("Weather Station ID")
);

CREATE TABLE "Weather_Dates" (
    "Weather Station ID" SMALLINT NOT NULL,
    "DATE" DATE NOT NULL,
    "AWND" REAL NOT NULL,
    "PGTM" TEXT,
    "PRCP" REAL NOT NULL,
    "SNOW" REAL NOT NULL,
    "SNWD" REAL NOT NULL,
    "TAVG" SMALLINT NOT NULL,
    "TMAX" SMALLINT NOT NULL,
    "TMIN" SMALLINT NOT NULL,
    "TSUN" TEXT,
    "WDF2" SMALLINT NOT NULL,
    "WDF5" REAL NOT NULL,
    "WSF2" REAL NOT NULL,
    "WSF5" REAL NOT NULL,
    PRIMARY KEY ("DATE", "TMAX")
);

CREATE TABLE "Trips" (
    "User ID" SMALLINT NOT NULL,
    "Start Station ID" SMALLINT NOT NULL,
    "End Station ID" SMALLINT NOT NULL,
    "Trip Duration" SMALLINT NOT NULL,
    "Start Time" TEXT NOT NULL,
    "Start Date" DATE NOT NULL,
    "Stop Time" TEXT NOT NULL,
    "Bike ID" SMALLINT NOT NULL,
    PRIMARY KEY ("Start Time", "Stop Time")
);

-- Add Foreign Key Constraints
ALTER TABLE "Trips" ADD CONSTRAINT "fk_Trips_User_ID" FOREIGN KEY ("User ID") REFERENCES "Users"("User ID");
ALTER TABLE "Trips" ADD CONSTRAINT "fk_Trips_Start_Station_ID" FOREIGN KEY ("Start Station ID") REFERENCES "Bike_Stations"("Station ID");
ALTER TABLE "Trips" ADD CONSTRAINT "fk_Trips_End_Station_ID" FOREIGN KEY ("End Station ID") REFERENCES "Bike_Stations"("Station ID");
ALTER TABLE "Weather_Dates" ADD CONSTRAINT "fk_Weather_Dates_Weather_Station_ID" FOREIGN KEY ("Weather Station ID") REFERENCES "Weather_Stations"("Weather Station ID");

-- Create Indexes
CREATE INDEX "idx_trips_user_id" ON "Trips"("User ID");
CREATE INDEX "idx_trips_start_station_id" ON "Trips"("Start Station ID");
CREATE INDEX "idx_trips_end_station_id" ON "Trips"("End Station ID");
CREATE INDEX "idx_trips_bike_id" ON "Trips"("Bike ID");
CREATE INDEX "idx_trips_start_date" ON "Trips"("Start Date");
CREATE INDEX "idx_bike_stations_station_name" ON "Bike_Stations"("Station Name");
CREATE INDEX "idx_bike_stations_latitude" ON "Bike_Stations"("Latitude");
CREATE INDEX "idx_bike_stations_longitude" ON "Bike_Stations"("Longitude");
CREATE INDEX "idx_weather_stations_station" ON "Weather_Stations"("Station");
CREATE INDEX "idx_weather_dates_weather_station_id" ON "Weather_Dates"("Weather Station ID");
CREATE INDEX "idx_weather_dates_date" ON "Weather_Dates"("DATE");