-- Dispjay the average temperature of all city in hbtn_0c_0 database in mysql server
SELECT `city`, AVG(`value`) AS avg_temp;
FROM `Temperature`
ORDER BY `avg_temp` DESC;
