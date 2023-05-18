-- list the max value of cities that has the same temperature
SELECT `city`, MAX(`value`) AS max_temp
FROM `Temperatures`
GROUP BY `state`
ORDER BY `state`;

