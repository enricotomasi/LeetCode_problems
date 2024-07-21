# Write your MySQL query statement below

DELETE a FROM Person a
INNER JOIN Person b 
WHERE 
    a.id > b.id AND 
    a.email = b.email;