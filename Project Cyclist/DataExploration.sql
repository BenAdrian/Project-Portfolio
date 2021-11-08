--Show all data
SELECT (*)
FROM ['divvy-tripdata$']

--Find Redundant
SELECT ride_id, COUNT(ride_id) 
FROM ['divvy-tripdata$']
GROUP BY ride_id
HAVING COUNT(ride_id) > 1

--Looking for time period
SELECT MAX(started_at), MIN(started_at)
FROM ['divvy-tripdata$']

--Calculate The Amount of Data
SELECT COUNT(*)
FROM ['divvy-tripdata$']

--Count the Membership
SELECT member_casual, COUNT((member_casual)) AS member_count
FROM ['divvy-tripdata$']
GROUP BY member_casual

--Search for the most used Start_Station
SELECT start_station_name, COUNT(*) AS station_count
FROM ['divvy-tripdata$']
GROUP BY start_station_name
ORDER BY 2 DESC

--Search for the most used End_Station
SELECT end_station_name, COUNT(*) AS station_count
FROM ['divvy-tripdata$']
GROUP BY end_station_name
ORDER BY 2 DESC


--Search for Favourite Route
SELECT TOP 5 start_station_name, end_station_name, COUNT(*) AS trips_count
FROM ['divvy-tripdata$']
WHERE start_station_name != end_station_name 
GROUP BY start_station_name, end_station_name
ORDER BY trips_count DESC

--Find who the most use the favourite route between the member
SELECT member_casual, COUNT(*) AS member_count
FROM ['divvy-tripdata$']
WHERE start_station_name IN
(SELECT TOP 5 start_station_name
FROM ['divvy-tripdata$']
WHERE start_station_name != end_station_name ) 
GROUP BY member_casual

--Looking for member usage per Week
SELECT member_casual,
COUNT(case when datepart(dd, started_at) >= '1' AND datepart(dd, started_at) <= '4' THEN 1 end) AS week_1,
COUNT(case when datepart(dd, started_at) >= '5' AND datepart(dd, started_at) <= '11' THEN 1 end) AS week_2,
COUNT(case when datepart(dd, started_at) >= '12' AND datepart(dd, started_at) <= '18' THEN 1 end) AS week_3,
COUNT(case when datepart(dd, started_at) >= '19' AND datepart(dd, started_at) <= '25' THEN 1 end) AS week_4,
COUNT(case when datepart(dd, started_at) >= '26' AND datepart(dd, started_at) <= '30' THEN 1 end) AS week_5
FROM ['divvy-tripdata$']
GROUP BY member_casual

--Looking for Member usage per Day
SELECT member_casual, day_of_week, COUNT(*) AS member_count
FROM ['divvy-tripdata$']
GROUP BY member_casual, day_of_week
ORDER BY day_of_week

--Average ride length Per day by Member
SELECT member_casual, day_of_week, ROUND(AVG(ride_length),0) AS average_in_minute
FROM ['divvy-tripdata$']
GROUP BY member_casual, day_of_week
ORDER BY day_of_week

--Users who use Above Average Time in April
SELECT member_casual, COUNT(member_casual) AS member_count
FROM ['divvy-tripdata$']
WHERE ride_length > (SELECT ROUND(AVG(ride_length),0) 
FROM ['divvy-tripdata$'])
GROUP BY member_casual

--Users who use Below Average Time in April
SELECT member_casual, COUNT(member_casual) AS member_count
FROM ['divvy-tripdata$']
WHERE ride_length < (SELECT ROUND(AVG(ride_length),0) 
FROM ['divvy-tripdata$'])
GROUP BY member_casual


