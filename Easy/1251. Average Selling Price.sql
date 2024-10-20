# Write your MySQL query statement below
SELECT DISTINCT(prices.product_id), IFNULL(ROUND(SUM(prices.price * unitssold.units) OVER win / SUM(unitssold.units) OVER win, 2), 0) AS average_price
FROM prices
LEFT JOIN unitssold ON prices.product_id = unitssold.product_id AND unitssold.purchase_date BETWEEN prices.start_date AND prices.end_date
WINDOW win AS (PARTITION BY prices.product_id);