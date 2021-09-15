```sql

-> 순서 지키기.
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
-> Y - 2018 y - 18 이런식으로 대소문자에 따라 값이 다름

7. 부속 질의문 -> IN, NOT IN, SOME, ALL 사용 가능

8. JOIN 에 관해서

A
ID val1
1 a
2 b
3 c
4 d
5 e

B
ID val2
2 ab
3 cd
5 ef
6 gh

ID va1 va2
1 a null -> LEFT
2 b ab ->  INNER, LEFT, RIGHT
3 c cd ->  INNER, LEFT, RIGHT
4 d null -> LEFT
5 e ef ->  INNER, LEFT, RIGHT
6 null gh -> RIGHT





```
