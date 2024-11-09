# Write your MySQL query statement below
SELECT Users.name as NAME, sum(Transactions.amount) AS BALANCE
FROM Users
JOIN Transactions ON Users.Account = Transactions.account
GROUP BY Users.name
HAVING BALANCE > 10000