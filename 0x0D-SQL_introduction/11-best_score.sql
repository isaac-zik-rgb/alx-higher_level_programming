-- list all records in mysql server
-- list records that scores >=10 in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= '10'
ORDER BY `score`DESC;
