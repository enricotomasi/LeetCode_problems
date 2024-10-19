# Write your MySQL query statement below
SELECT Prices.product_id, ROUND(SUM(Prices.price * UnitsSold.units) / SUM(UnitsSold.units), 2) as average_price
FROM Prices
JOIN UnitsSold on Prices.product_id = UnitsSold.product_id AND purchase_date BETWEEN start_date AND end_date
GROUP BY Prices.product_id;