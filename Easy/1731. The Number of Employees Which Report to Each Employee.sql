# Write your MySQL query statement below
SELECT Employees.employee_id, Employees.name, COUNT(Employees.employee_id) AS reports_count, ROUND(avg(emp.age)) AS average_age
FROM Employees
JOIN Employees emp ON Employees.employee_id = emp.reports_to 
GROUP BY Employees.employee_id, Employees.name
ORDER BY Employees.employee_id
