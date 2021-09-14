```sql

SELECT 보고싶은 칼럼
FROM table명
WHERE 조건
GROUP BY 묶는 기준
ORDER BY 정렬 기준
LIKE 문자열 조건
LIMIT 보고싶은 갯수
OFFSET 앞에서부터 ~개 빼고

1. LIMIT n -> 상위 n개 뽑고싶을때

2. HOUR(DATETIME) -> 시간 구할 때 MINUTE, DAY, ...

3. IFNULL(NAME, "No name") -> NULL 처리

4. WHERE A LIKE "ABC%" # ABC로 시작하는 문자열
4-2 "%ABC" # ABC로 끝나는 문자열
4-3 "%ABC%" # ABC가 포함된 문자열
4-4 "abc_ _ _" # abc로 시작하는 6자리 문자열

5. SELECT IF(SEX_UPON_INTAKE LIKE '%Neutered%', "O", "X") as "중성화"
-> Neutered라는 단어가 들어가 있으면 "O" 아니면 "X"로 표시

6. DATE_FORMAT(DATETIME,'%Y-%m-%d') as "날짜" # date format



```
