-- list number of record with the same score in the second_table in my sql server
-- records will be ordered by descending count
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
