# Write your MySQL query statement below
SELECT a.employee_id 
FROM Employees a
WHERE (a.salary < 30000 AND a.manager_id IS NOT NULL AND NOT EXISTS (SELECT * FROM Employees b WHERE b.employee_id = a.manager_id))
ORDER BY a.employee_id
