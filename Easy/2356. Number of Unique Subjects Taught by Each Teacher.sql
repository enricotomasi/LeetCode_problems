# Write your MySQL query statement below
SELECT a.teacher_id, count(DISTINCT subject_id) as cnt
FROM Teacher AS a
GROUP BY a.teacher_id