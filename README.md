# mybikes
## Description
In this project, I used data from the [HealthyRidePGH website](https://healthyridepgh.com/) where I performed some trivial tasks using Python. Such as:
1. Finding the total bikes availble at a given station 
2. Finding the total number of availble bike docks at a given station 
3. Finding the percentage of total bikes at a given station 
4. Finding the 3 closest stations given a GPS coordinate 
5. Find the closest station with availble bikes

## Run Instructions with examples
This program takes different parameters based on the task. An example of the base command is
`python mybikes.py baseURL command [parameters]`  
Where the baseURL is https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en

### Task 1 - Finding the total bikes availble
`python mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_bikes`

### Task 2 - Finding total number of docks
`python mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_docks`

### Task 3 - Percentage of total docks
`python mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ percent_avail 342885`

### Task 4 - Find 3 closest stations
`python mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_stations 40.444618 -79.954707`

### Task 5 - Find closest station with bikes
`python mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_bike 40.444618 -79.954707`

