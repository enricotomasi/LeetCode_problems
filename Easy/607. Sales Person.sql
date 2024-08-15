# Write your MySQL query statement below
SELECT salesPerson.name
FROM salesPerson
WHERE salesPerson.sales_id NOT IN
(
    SELECT orders.sales_id FROM orders
    LEFT JOIN company
    ON orders.com_id = company.com_id
    WHERE name="RED"
)