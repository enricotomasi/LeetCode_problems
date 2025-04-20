# Write your MySQL query statement below
SELECT *
FROM products
WHERE description REGEXP 'SN+[0-9]{4}+[-]+[0-9]{4}' AND description NOT REGEXP 'SN+[0-9]{4}+[-]+[0-9]{5}'
ORDER BY product_id