# Write your MySQL query statement below
SELECT Customers.name as Customers
FROM Customers
WHERE NOT EXISTS (SELECT * FROM Orders where customerId = Customers.id)