SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') as "날짜"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID