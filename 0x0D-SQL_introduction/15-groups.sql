-- list number of record with the same score in the second_table in my sql server
-- score wipl be order in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
GROUP BY `number` DESC;
