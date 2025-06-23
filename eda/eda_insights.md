# Citibike Data Engineering - EDA Insights
## Introduction
This document contains insights from the EDA notebooks. It is designed to be dynamic and reusable, allowing for easy updates with new insights.
## Data Inspection
This section provides an overview of the data structure and possible foreign key insights from the EDA notebook - 1_data_structure_inspection.ipynb.
### Newark Airport Table Overview
| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| STATION |  | object | ['USW00014734'] | 1 |
| NAME |  | object | ['NEWARK LIBERTY INTERNATIONAL AIRPORT, NJ US'] | 1 |
| DATE |  | object | ['2016-01-01' '2016-01-02' '2016-01-03'] | 366 |
| AWND |  | float64 | [12.75  9.4  10.29] | 70 |
| PGTM |  | float64 | [] | 0 |
| PRCP |  | float64 | [0.   0.01 1.77] | 56 |
| SNOW |  | float64 | [0.  0.7 0.5] | 11 |
| SNWD |  | float64 | [0.  1.2 7.1] | 12 |
| TAVG |  | int64 | [41 36 37] | 69 |
| TMAX |  | int64 | [43 42 47] | 74 |
| TMIN |  | int64 | [34 30 28] | 69 |
| TSUN |  | float64 | [] | 0 |
| WDF2 |  | int64 | [270 260 330] | 34 |
| WDF5 |  | float64 | [280. 260. 250.] | 35 |
| WSF2 |  | float64 | [25.9 21.  23.9] | 32 |
| WSF5 |  | float64 | [35.1 25.1 30. ] | 44 |

### Citibike Table Overview
| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| index | Original index of the DataFrame | int64 | [0 1 2] | 34149 |
| Trip Duration | Duration of the trip in seconds | int64 | [362 200 202] | 6024 |
| Start Time | Start time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:02:52' '2016-01-01 00:18:22' '2016-01-01 00:18:25'] | 244407 |
| Stop Time | End time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:08:54' '2016-01-01 00:21:42' '2016-01-01 00:21:47'] | 244137 |
| Start Station ID | Unique identifier for the start station | int64 | [3186 3209 3195] | 51 |
| Start Station Name | Name of the start station | object | ['Grove St PATH' 'Brunswick St' 'Sip Ave'] | 51 |
| Start Station Latitude | Latitude of the start station | float64 | [40.71958612 40.7241765  40.73074263] | 51 |
| Start Station Longitude | Longitude of the start station | float64 | [-74.04311746 -74.0506564  -74.06378388] | 51 |
| End Station ID | Unique identifier for the end station | int64 | [3209 3213 3203] | 102 |
| End Station Name | Name of the end station | object | ['Brunswick St' 'Van Vorst Park' 'Hamilton Park'] | 102 |
| End Station Latitude | Latitude of the end station | float64 | [40.7241765  40.71848892 40.72759597] | 102 |
| End Station Longitude | Longitude of the end station | float64 | [-74.0506564  -74.04772662 -74.04424731] | 102 |
| Bike ID | Unique identifier for the bike used in the trip | int64 | [24647 24605 24689] | 566 |
| User Type | Type of user (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member) | object | ['Subscriber' 'Customer'] | 2 |
| Birth Year | Year of birth of the user | float64 | [1964. 1962. 1984.] | 64 |
| Gender | Gender of the user (0: Unknown, 1: Male, 2: Female) | int64 | [2 1 0] | 3 |

## Possible Foreign Key Relationships
This section provides an overview of the possible foreign key relationships between the datasets.
| df1_column | df2_column | match_ratio | comment |
| --- | --- | --- | --- |
| citibike_df.Trip Date | newark_airport_df.DATE | 1.0 | Possible foreign key match |

# Citibike Data Engineering - EDA Insights

## Introduction
This document contains insights from the EDA notebooks. It is designed to be dynamic and reusable, allowing for easy updates with new insights.

## Data Inspection
This section provides an overview of the data structure and possible foreign key insights from the EDA notebook - 1_data_structure_inspection.ipynb.

### Newark Airport Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| STATION |  | object | ['USW00014734'] | 1 |
| NAME |  | object | ['NEWARK LIBERTY INTERNATIONAL AIRPORT, NJ US'] | 1 |
| DATE |  | object | ['2016-01-01' '2016-01-02' '2016-01-03'] | 366 |
| AWND |  | float64 | [12.75  9.4  10.29] | 70 |
| PGTM |  | float64 | [] | 0 |
| PRCP |  | float64 | [0.   0.01 1.77] | 56 |
| SNOW |  | float64 | [0.  0.7 0.5] | 11 |
| SNWD |  | float64 | [0.  1.2 7.1] | 12 |
| TAVG |  | int64 | [41 36 37] | 69 |
| TMAX |  | int64 | [43 42 47] | 74 |
| TMIN |  | int64 | [34 30 28] | 69 |
| TSUN |  | float64 | [] | 0 |
| WDF2 |  | int64 | [270 260 330] | 34 |
| WDF5 |  | float64 | [280. 260. 250.] | 35 |
| WSF2 |  | float64 | [25.9 21.  23.9] | 32 |
| WSF5 |  | float64 | [35.1 25.1 30. ] | 44 |


### Citibike Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| index | Original index of the DataFrame | int64 | [0 1 2] | 34149 |
| Trip Duration | Duration of the trip in seconds | int64 | [362 200 202] | 6024 |
| Start Time | Start time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:02:52' '2016-01-01 00:18:22' '2016-01-01 00:18:25'] | 244407 |
| Stop Time | End time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:08:54' '2016-01-01 00:21:42' '2016-01-01 00:21:47'] | 244137 |
| Start Station ID | Unique identifier for the start station | int64 | [3186 3209 3195] | 51 |
| Start Station Name | Name of the start station | object | ['Grove St PATH' 'Brunswick St' 'Sip Ave'] | 51 |
| Start Station Latitude | Latitude of the start station | float64 | [40.71958612 40.7241765  40.73074263] | 51 |
| Start Station Longitude | Longitude of the start station | float64 | [-74.04311746 -74.0506564  -74.06378388] | 51 |
| End Station ID | Unique identifier for the end station | int64 | [3209 3213 3203] | 102 |
| End Station Name | Name of the end station | object | ['Brunswick St' 'Van Vorst Park' 'Hamilton Park'] | 102 |
| End Station Latitude | Latitude of the end station | float64 | [40.7241765  40.71848892 40.72759597] | 102 |
| End Station Longitude | Longitude of the end station | float64 | [-74.0506564  -74.04772662 -74.04424731] | 102 |
| Bike ID | Unique identifier for the bike used in the trip | int64 | [24647 24605 24689] | 566 |
| User Type | Type of user (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member) | object | ['Subscriber' 'Customer'] | 2 |
| Birth Year | Year of birth of the user | float64 | [1964. 1962. 1984.] | 64 |
| Gender | Gender of the user (0: Unknown, 1: Male, 2: Female) | int64 | [2 1 0] | 3 |


## Possible Foreign Key Relationships
This section provides an overview of the possible foreign key relationships between the datasets.

| df1_column | df2_column | match_ratio | comment |
| --- | --- | --- | --- |
| citibike_df.Trip Date | newark_airport_df.DATE | 1.0 | Possible foreign key match |


# Citibike Data Engineering - EDA Insights

## Introduction
This document contains insights from the EDA notebooks. It is designed to be dynamic and reusable, allowing for easy updates with new insights.

## Data Inspection
This section provides an overview of the data structure and possible foreign key insights from the EDA notebook - 1_data_structure_inspection.ipynb.

### Newark Airport Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| STATION |  The station identification code | object | ['USW00014734'] | 1 |
| NAME | Name of the station (Newark Airport) | object | ['NEWARK LIBERTY INTERNATIONAL AIRPORT, NJ US'] | 1 |
| DATE | Date of the observation (YYYY-MM-DD) | object | ['2016-01-01' '2016-01-02' '2016-01-03'] | 366 |
| AWND | Average wind speed (miles per hour) | float64 | [12.75  9.4  10.29] | 70 |
| PGTM | Peak gust time (HHMM) | float64 | [] | 0 |
| PRCP | Precipitation (inches) | float64 | [0.   0.01 1.77] | 56 |
| SNOW | Snowfall (inches) | float64 | [0.  0.7 0.5] | 11 |
| SNWD | Snow depth (inches) | float64 | [0.  1.2 7.1] | 12 |
| TAVG | Average temperature (degrees Fahrenheit) | int64 | [41 36 37] | 69 |
| TMAX | Maximum temperature (degrees Fahrenheit) | int64 | [43 42 47] | 74 |
| TMIN | Minimum temperature (degrees Fahrenheit) | int64 | [34 30 28] | 69 |
| TSUN | Total sunshine (minutes) | float64 | [] | 0 |
| WDF2 | Direction of fastest 2-minute wind (degrees) | int64 | [270 260 330] | 34 |
| WDF5 | Direction of fastest 5-second wind (degrees) | float64 | [280. 260. 250.] | 35 |
| WSF2 | Fastest 2-minute wind speed (miles per hour) | float64 | [25.9 21.  23.9] | 32 |
| WSF5 | Fastest 5-second wind speed (miles per hour) | float64 | [35.1 25.1 30. ] | 44 |


### Citibike Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| index | Original index of the DataFrame | int64 | [0 1 2] | 34149 |
| Trip Duration | Duration of the trip in seconds | int64 | [362 200 202] | 6024 |
| Start Time | Start time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:02:52' '2016-01-01 00:18:22' '2016-01-01 00:18:25'] | 244407 |
| Stop Time | End time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:08:54' '2016-01-01 00:21:42' '2016-01-01 00:21:47'] | 244137 |
| Start Station ID | Unique identifier for the start station | int64 | [3186 3209 3195] | 51 |
| Start Station Name | Name of the start station | object | ['Grove St PATH' 'Brunswick St' 'Sip Ave'] | 51 |
| Start Station Latitude | Latitude of the start station | float64 | [40.71958612 40.7241765  40.73074263] | 51 |
| Start Station Longitude | Longitude of the start station | float64 | [-74.04311746 -74.0506564  -74.06378388] | 51 |
| End Station ID | Unique identifier for the end station | int64 | [3209 3213 3203] | 102 |
| End Station Name | Name of the end station | object | ['Brunswick St' 'Van Vorst Park' 'Hamilton Park'] | 102 |
| End Station Latitude | Latitude of the end station | float64 | [40.7241765  40.71848892 40.72759597] | 102 |
| End Station Longitude | Longitude of the end station | float64 | [-74.0506564  -74.04772662 -74.04424731] | 102 |
| Bike ID | Unique identifier for the bike used in the trip | int64 | [24647 24605 24689] | 566 |
| User Type | Type of user (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member) | object | ['Subscriber' 'Customer'] | 2 |
| Birth Year | Year of birth of the user | float64 | [1964. 1962. 1984.] | 64 |
| Gender | Gender of the user (0: Unknown, 1: Male, 2: Female) | int64 | [2 1 0] | 3 |


## Possible Foreign Key Relationships
This section provides an overview of the possible foreign key relationships between the datasets.

| df1_column | df2_column | match_ratio | comment |
| --- | --- | --- | --- |
| citibike_df.Trip Date | newark_airport_df.DATE | 1.0 | Possible foreign key match |


# Citibike Data Engineering - EDA Insights

## Introduction
This document contains insights from the EDA notebooks. It is designed to be dynamic and reusable, allowing for easy updates with new insights.

## Data Inspection
This section provides an overview of the data structure and possible foreign key insights from the EDA notebook - 1_data_structure_inspection.ipynb.

### Newark Airport Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| STATION |  The station identification code | object | ['USW00014734'] | 1 |
| NAME | Name of the station (Newark Airport) | object | ['NEWARK LIBERTY INTERNATIONAL AIRPORT, NJ US'] | 1 |
| DATE | Date of the observation (YYYY-MM-DD) | object | ['2016-01-01' '2016-01-02' '2016-01-03'] | 366 |
| AWND | Average wind speed (miles per hour) | float64 | [12.75  9.4  10.29] | 70 |
| PGTM | Peak gust time (HHMM) | float64 | [] | 0 |
| PRCP | Precipitation (inches) | float64 | [0.   0.01 1.77] | 56 |
| SNOW | Snowfall (inches) | float64 | [0.  0.7 0.5] | 11 |
| SNWD | Snow depth (inches) | float64 | [0.  1.2 7.1] | 12 |
| TAVG | Average temperature (degrees Fahrenheit) | int64 | [41 36 37] | 69 |
| TMAX | Maximum temperature (degrees Fahrenheit) | int64 | [43 42 47] | 74 |
| TMIN | Minimum temperature (degrees Fahrenheit) | int64 | [34 30 28] | 69 |
| TSUN | Total sunshine (minutes) | float64 | [] | 0 |
| WDF2 | Direction of fastest 2-minute wind (degrees) | int64 | [270 260 330] | 34 |
| WDF5 | Direction of fastest 5-second wind (degrees) | float64 | [280. 260. 250.] | 35 |
| WSF2 | Fastest 2-minute wind speed (miles per hour) | float64 | [25.9 21.  23.9] | 32 |
| WSF5 | Fastest 5-second wind speed (miles per hour) | float64 | [35.1 25.1 30. ] | 44 |


### Citibike Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| index | Original index of the DataFrame | int64 | [0 1 2] | 34149 |
| Trip Duration | Duration of the trip in seconds | int64 | [362 200 202] | 6024 |
| Start Time | Start time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:02:52' '2016-01-01 00:18:22' '2016-01-01 00:18:25'] | 244407 |
| Stop Time | End time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:08:54' '2016-01-01 00:21:42' '2016-01-01 00:21:47'] | 244137 |
| Start Station ID | Unique identifier for the start station | int64 | [3186 3209 3195] | 51 |
| Start Station Name | Name of the start station | object | ['Grove St PATH' 'Brunswick St' 'Sip Ave'] | 51 |
| Start Station Latitude | Latitude of the start station | float64 | [40.71958612 40.7241765  40.73074263] | 51 |
| Start Station Longitude | Longitude of the start station | float64 | [-74.04311746 -74.0506564  -74.06378388] | 51 |
| End Station ID | Unique identifier for the end station | int64 | [3209 3213 3203] | 102 |
| End Station Name | Name of the end station | object | ['Brunswick St' 'Van Vorst Park' 'Hamilton Park'] | 102 |
| End Station Latitude | Latitude of the end station | float64 | [40.7241765  40.71848892 40.72759597] | 102 |
| End Station Longitude | Longitude of the end station | float64 | [-74.0506564  -74.04772662 -74.04424731] | 102 |
| Bike ID | Unique identifier for the bike used in the trip | int64 | [24647 24605 24689] | 566 |
| User Type | Type of user (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member) | object | ['Subscriber' 'Customer'] | 2 |
| Birth Year | Year of birth of the user | float64 | [1964. 1962. 1984.] | 64 |
| Gender | Gender of the user (0: Unknown, 1: Male, 2: Female) | int64 | [2 1 0] | 3 |


## Possible Foreign Key Relationships
This section provides an overview of the possible foreign key relationships between the datasets.

| df1_column | df2_column | match_ratio | comment |
| --- | --- | --- | --- |
| citibike_df.Trip Date | newark_airport_df.DATE | 1.0 | Possible foreign key match |


# Citibike Data Engineering - EDA Insights

## Introduction
This document contains insights from the EDA notebooks. It is designed to be dynamic and reusable, allowing for easy updates with new insights.

## Data Inspection
This section provides an overview of the data structure and possible foreign key insights from the EDA notebook - 1_data_structure_inspection.ipynb.

### Newark Airport Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| STATION |  The station identification code | object | ['USW00014734'] | 1 |
| NAME | Name of the station (Newark Airport) | object | ['NEWARK LIBERTY INTERNATIONAL AIRPORT, NJ US'] | 1 |
| DATE | Date of the observation (YYYY-MM-DD) | object | ['2016-01-01' '2016-01-02' '2016-01-03'] | 366 |
| AWND | Average wind speed (miles per hour) | float64 | [12.75  9.4  10.29] | 70 |
| PGTM | Peak gust time (HHMM) | float64 | [] | 0 |
| PRCP | Precipitation (inches) | float64 | [0.   0.01 1.77] | 56 |
| SNOW | Snowfall (inches) | float64 | [0.  0.7 0.5] | 11 |
| SNWD | Snow depth (inches) | float64 | [0.  1.2 7.1] | 12 |
| TAVG | Average temperature (degrees Fahrenheit) | int64 | [41 36 37] | 69 |
| TMAX | Maximum temperature (degrees Fahrenheit) | int64 | [43 42 47] | 74 |
| TMIN | Minimum temperature (degrees Fahrenheit) | int64 | [34 30 28] | 69 |
| TSUN | Total sunshine (minutes) | float64 | [] | 0 |
| WDF2 | Direction of fastest 2-minute wind (degrees) | int64 | [270 260 330] | 34 |
| WDF5 | Direction of fastest 5-second wind (degrees) | float64 | [280. 260. 250.] | 35 |
| WSF2 | Fastest 2-minute wind speed (miles per hour) | float64 | [25.9 21.  23.9] | 32 |
| WSF5 | Fastest 5-second wind speed (miles per hour) | float64 | [35.1 25.1 30. ] | 44 |


### Citibike Table Overview

| Column Name | Description | Data Type | Value Examples | Value Distinct Count |
| --- | --- | --- | --- | --- |
| index | Original index of the DataFrame | int64 | [0 1 2] | 34149 |
| Trip Duration | Duration of the trip in seconds | int64 | [362 200 202] | 6024 |
| Start Time | Start time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:02:52' '2016-01-01 00:18:22' '2016-01-01 00:18:25'] | 244407 |
| Stop Time | End time of the trip (YYYY-MM-DD HH:MM:SS) | object | ['2016-01-01 00:08:54' '2016-01-01 00:21:42' '2016-01-01 00:21:47'] | 244137 |
| Start Station ID | Unique identifier for the start station | int64 | [3186 3209 3195] | 51 |
| Start Station Name | Name of the start station | object | ['Grove St PATH' 'Brunswick St' 'Sip Ave'] | 51 |
| Start Station Latitude | Latitude of the start station | float64 | [40.71958612 40.7241765  40.73074263] | 51 |
| Start Station Longitude | Longitude of the start station | float64 | [-74.04311746 -74.0506564  -74.06378388] | 51 |
| End Station ID | Unique identifier for the end station | int64 | [3209 3213 3203] | 102 |
| End Station Name | Name of the end station | object | ['Brunswick St' 'Van Vorst Park' 'Hamilton Park'] | 102 |
| End Station Latitude | Latitude of the end station | float64 | [40.7241765  40.71848892 40.72759597] | 102 |
| End Station Longitude | Longitude of the end station | float64 | [-74.0506564  -74.04772662 -74.04424731] | 102 |
| Bike ID | Unique identifier for the bike used in the trip | int64 | [24647 24605 24689] | 566 |
| User Type | Type of user (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member) | object | ['Subscriber' 'Customer'] | 2 |
| Birth Year | Year of birth of the user | float64 | [1964. 1962. 1984.] | 64 |
| Gender | Gender of the user (0: Unknown, 1: Male, 2: Female) | int64 | [2 1 0] | 3 |


## Possible Foreign Key Relationships
This section provides an overview of the possible foreign key relationships between the datasets.

| df1_column | df2_column | match_ratio | comment |
| --- | --- | --- | --- |
| citibike_df.Trip Date | newark_airport_df.DATE | 1.0 | Possible foreign key match |


