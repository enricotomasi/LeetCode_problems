# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating/position), 2) AS quality, 
       ROUND(SUM(IF(rating < 3, 1, 0))/COUNT(rating)*100,2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;