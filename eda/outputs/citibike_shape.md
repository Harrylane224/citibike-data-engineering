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
