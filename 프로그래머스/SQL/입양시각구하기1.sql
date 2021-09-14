SELECT HOUR(DATETIME) as HOUR, COUNT(DATETIME) as COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME) 
ORDER BY HOUR