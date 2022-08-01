-- See al the Data in this data set
SELECT TOP 10 *
FROM AB_NYC_2019$

--Total of the location
SELECT COUNT(DISTINCT neighbourhood) AS total_location
FROM AB_NYC_2019$
WHERE neighbourhood IS NOT NULL

--Average Price
SELECT ROUND(AVG(price), 2) as average_price
FROM AB_NYC_2019$
WHERE price IS NOT NULL AND price !< 0;

--Total of the Property
SELECT COUNT(DISTINCT name) AS total_place
FROM AB_NYC_2019$

--Total host
SELECT COUNT(DISTINCT host_id) AS total_host
FROM AB_NYC_2019$

--Count Room by Location
SELECT TOP 5 neighbourhood_group, COUNT(*) as total_room
FROM AB_NYC_2019$
GROUP BY neighbourhood_group
ORDER BY total_room DESC;

-- Total Room Type by Neighbourhood Group
SELECT TOP 5 neighbourhood_group, 
SUM(CASE WHEN room_type = 'Private room' THEN 1 ELSE 0 END) AS private_room,
SUM(CASE WHEN room_type = 'Entire home/apt' THEN 1 ELSE 0 END) AS entire_home_or_apt,
SUM(CASE WHEN room_type = 'Shared room' THEN 1 ELSE 0 END) AS shared_room,
COUNT(room_type) AS total_room
FROM AB_NYC_2019$
GROUP BY neighbourhood_group
ORDER BY total_room DESC;

--Type Room location and price
SELECT neighbourhood_group, room_type, ROUND(AVG(price), 2) AS average_price
FROM AB_NYC_2019$
WHERE room_type IS NOT NULL AND room_type NOT LIKE '%[123456789%]%' AND price IS NOT NULL AND price !< 0
GROUP BY neighbourhood_group, room_type
ORDER BY average_price DESC


--Top 5 host with most listing
SELECT TOP 5 host_id, host_name, COUNT(name) as Total
FROM AB_NYC_2019$
WHERE name IS NOT NULL AND host_name IS NOT NULL
GROUP BY host_id, host_name
ORDER BY Total DESC;

--Count of Room Type
SELECT room_type, COUNT(*) as room_count
FROM AB_NYC_2019$
WHERE room_type IS NOT NULL AND room_type NOT LIKE '%[123456789%]%'
GROUP BY room_type
ORDER BY room_count DESC;







