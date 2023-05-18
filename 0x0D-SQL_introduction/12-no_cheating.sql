-- update the name Bob with the score 10
-- list ib descending order in mysql sever
SELECT `score`, `name`
FROM `second_table`
WHERE `name` = "Bob"
UPDATE `score` = '10'
ORDER BY `score` DESC;
