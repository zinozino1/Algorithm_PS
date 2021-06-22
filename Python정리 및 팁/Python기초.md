```py

1. 변수와 출력 함수

* 파이썬 같은 경우는 변수의 유효범위가 함수를 기준으로 생성 JS의 var와 같다

* 변수명 정하기
1) 영문과 숫자, _로 이루어진다
2) 대소문자를 구분한다. a 와 A는 다름
a = 1
A = 2
print(a,A) => 1 2 출력

3) 문자나, _로 시작한다
4) 특수문자, 키워드 사용하면 안됨


* 나열 하여 대입 가능

a, b, c = 10, 2, 1
print(a, b, c)
a, b, c = 1, 2, 3
print(a, b, c) --> 재할당 가능



* 값 교환

a, b = 10, 20
print(a, b) // 10, 20
a, b = b, a
print(a, b) // 20, 10



* 변수 타입

a = 12314 -> 4바이트
print(type(a))
print(a)

a = 123.123123123123 -> 8바이트
print(type(a))
print(a)

a = 1.123123123123123213131231 -> 8바이트
print(type(a))
print(a)

= 결과
<type 'int'>
12314
<type 'float'>
123.123123123
<type 'float'>
1.12312312312


a = "str" // string 싱글, 더블 따옴표 둘 다 가능
print(type(a))
<type 'str'>



* 출력방식

a, b, c = 1, 2, 3
print(a, b, c) // 1 2 3
print(a, b, c, sep=", ") // 1, 2, 3
print(a, b, c, sep=",") // 1,2,3
print(a, b, c, sep="\n") //
1
2
3
print(a, end=" ") -> print 는 기본적으로 줄바꿈을 한다.
print(b)
print(c) //
1 2
3




2. 변수 입력과 연산자

* 사용자 입력 받기

-> input 함수는 "한 줄"의 문자열을 입력받는다.

a = input() // 입력
print(a) // 출력

a = input("입력하세요 : ")
print(a)

a, b = input("두 숫자를 입력하세요").split() // 2 3
print(a + b) // 23 -> 문자로 입력이 되어서 붙어버린다

type 이 str임.


* 코딩테스트 전형적 입력 방법 -> 복붙 가능

경우 1)
n = int(input())
arr = list(map(int, input().split()))

print(n)
print(arr)

경우 2)
a, b = map(int, input().split())

* 코딩테스트 전형적 문자열 입력 방법(input 보다 훨씬 빠른속도)

import sys
data = sys.stdin.readline().rstrip()

경우 3)

* 입력 숫자 값이 매우 많을 때

k, n = map(int, input().split())
a = [int(sys.stdin.readline()) for _ in range(k)]

*** split 함수
-> 디폴트는 띄어쓰기 입력
-> 인자 넣으면 인자에 따라 입력 가능
a,b = input().split('.') -> \n 은 안되는듯?
print(a,b)


* 형변환

a, b = input("숫자를 입력하세요: ").split()
a = int(a) // int형
a = float(a) // float형
print(type(a))


a, b, c = map(int, input("숫자를 입력하세요: ").split()) // 한꺼번에 미리 형변환 map 함수 이용
print(a, b, c)
-> 띄어쓰기 입력밖에?


* map 함수 -> JS의 배열 고차함수 map 과 비슷하다고 생각.

파이썬의 내장 함수인 map()는 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용됩니다. 따라서, 여러 개의 데이터를 담고 있는 list나 tuple을 대상으로 주로 사용하는 함수입니다.

사용 방법은 매우 간단한데요… 기본 문법은 다음과 같습니다.

map(변환 함수, 순회 가능한 데이터)

** int 도 내장 함수임. integer로 변환하는 함수

*** 하나만 변환할거면 int(input()) 이런식으로.


* 연산

a, b = map(int, input("숫자를 입력하세요: ").split())
-> 이말인 즉슨 input().split()이 이터러블이란 것

입력 : 10 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) // 나누기 -> 5.0
print(a // b) // 몫 -> 5
print(a % b) // 나머지 -> 0
print(a ** b) // 거듭제곱 -> 100



a = 4.3
b = 5
c = a + b // 실수 + 정수 = 실수(더 큰 범위가 나옴)
print(type(c))


* 지수표현

1e9 = 1000000000   ~> 10억


* 반올림

round(실수형 데이터, 반올림하고자 하는 위치 -1)
round(423.456, 2)  ~> 423.46


*** round half even 방식을 택하자

a = 66.5
a = a + 0.5
a = int(a) -> 이것이 더 오류 적음


**** in, not in -> 빌트인 자료형(리스트, 문자열, 튜플, 딕셔너리, 셋)에 모두 사용 가능

arr = [1, 2, 3, 4] // list
s1 = {1, 2, 3} // set
d = {"1": 1, "2": 2} // dict
t = (1, 2, 3) // tuple
msg = "Hi im Ted" // str

print(2 in arr) # True
print(1 not in arr) # False
print(2 in s1) # True
print("1" in d) # True -> key값으로 판단
print(1 in d) # False
print(3 in t) # True
print(' ' in msg) # True


* 파이썬의 삼항 연산자 -> 잘 안 쓰는듯?

print("True는 참" if True else "True는 거짓")
-> true ? "True는 참" : "True는 거짓"
print("False는 참" if False else "False는 거짓")




3. 조건문

* 조건

x = 7

if x == 7:
    print("같습니다")
    print("히히")
else:
    print("키키")

// 중괄호가 없음. 들여쓰기 신경써야함, 콜론 주의


* 논리 및 비교 연산자 활용
x = 7
if x > 0 and x < 10 and type(x) == int:
    print("10보다 작은 자연수") // "&& == and" "|| == or"


* 더 쉬운 방법. 파이썬만 되는 미친 문법
x = 7
if 0 < x < 7 and type(x) == int:
    print("zlzl")


* 분기

x = -10

if x > 0:
    print("양수")
else:
    print("음수")


* 다중 if

x = 93

if x >= 90: // A,B,C 다 출력하지 않는다. if elif 문의 특징
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
else:
    print("F")




4. 반복문

* range 함수

a = range(10) // 순차적으로 정수 리스트를 만듦 0부터 range - 1까지
-> 아직 실체화 x
print(list(a)) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> 실체화 o

a = range(1, 10) // 앞의 숫자는 포함 뒤의 숫자는 -1
b = range(1, 11)
print(list(a)) // [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(b)) // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



for i in range(5): // 콜론 넣어주기 주의
    print("heelo", end=" ") // heelo heelo heelo heelo heelo

for i in range(1, 10):
    print(i) // 1부터 9까지 줄바꿈 출력

for i in range(10):
    print(i) // 0부터 9까지 줄바꿈 출력


* 역순

for i in range(10, 0): // 아무것도 출력 x
    print(i)

for i in range(10, 0, -1): // 10, 9, 8...1
    print(i)

for i in range(10, 0, -2): // 10, 8, 6...2
    print(i)


* while

i = 10

while i >= 1:
    print(i)
    i -= 1 // 파이썬에는 증감 연산자 없음


i = 1

while True: // 무한 루프
    print(1)

i = 1

while True: // break 는 다른 언어와 동일
    if i > 10:
        break
    print(i)
    i += 1

for i in range(1, 11): // continue 도 마찬가지
    if i % 2 == 0:
        continue
    print(i)



* for else 문

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else: // for 문이 break 에 의해 종료되었다면 else문 실행 x
    print(11)

for i in range(1, 11):
    print(i)
    if i > 15:
        break
else: // for문이 다 돌았다면(정상적으로 돌았다면) else문 실행
    print(11)





5. 반복문을 이용한 문제 풀이

n = int(input())


1) 1부터 N 까지 홀수 출력

for i in range(1, n):
    if i % 2 == 0:
        continue
    print(i)

2) 1부터 N 까지의 합 구하기

sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

* result = sum(list(range(n + 1))) // 이렇게도 가능

3) N의 약수 출력하기

for i in range(1, n + 1):
    if n % i != 0:
        continue
    print(i)





6. 중첩 반복문

별찍기.




7. 문자열과 내장 함수

str = "Time is Now!"

0) 간단한 문자열 연산

a = "Hello"
b = "World"
print(a + " " + b) ~> Hello World

a = "String"
print(a * 3) ~> StringStringString


**** 주의점 문자열 연산은 문자열끼리 밖에 되지 않음

answer = 10
print("정답은" + answer + "입니다.") // error

-> 1)
print("정답은 " + str(answer) + " 입니다.") // ok
-> 2)
print("정답은", answer, "입니다.") // ok

=> 공백 주의

0) 문자가 숫자인가? - char.isdecimal() & isdigit()도 되는듯

1) 대문자화 - str.upper() // 반환 값 존재
-> side effect x

2) 소문자화 - str.lower() // 반환 값 존재
-> side effect x

3) 문자 찾기 - str.find(문자, [,index]) // 반환 값 존재
-> side effect x

4) 문자 들어간 갯수 - str.count(문자) // 반환 값 존재
-> side effect x

5) 문자열 슬라이스 - str[[,숫자1]:숫자2] -> 문자열은 내부적으로 리스트랑 비슷
-> side effect x // 반환 값 존재
* 숫자1번째 인덱스부터 숫자2 - 1 까지 슬라이스 숫자1 없으면 0부터
str[::-1] : 리버싱
str[i:j:k] -> range 에 들어가는 것과 비슷하다고 생각하면 됨

6) 문자열 길이 - len(str) // 반환 값 존재
-> side effect x
for i in range(len(str)):
    print(str[i])

for i in str: // 응용
    print(i, end="")

for i in str: // 응용 - 대문자만 출력
    if i.isupper():
        print(i)

for i in str: // 응용 - 공백 제거(알파벳만 출력)
    if i.isalpha():
        print(i, end="")

tmp='AZ' // 응용 아스키 코드 출력
for x in tmp:
    print(ord(x))

<->

tmp = 65
print(chr(tmp)) // 아스키 코드를 문자로

7) str.replace


text = '123,456,789,999'

replaceAll= text.replace(",","")
replace_t1 = text.replace(",", "",1)
replace_t2 = text.replace(",", "",2)
replace_t3 = text.replace(",", "",3)
print("결과 :")
print(replaceAll)
print(replace_t1)
print(replace_t2)
print(replace_t3)

'''
결과 :
123456789999
123456,789,999
123456789,999
123456789999
'''

8) 문자열 입력 개행문자 제거
** import sys, input = sys.stdin.readline 했을 경우만

-> 보통의 경우 : str = input() = "ABCD\n"
print(len(str)) => 5
print(str[-1]) => "/n"

-> 공백 제거한 경우 str = input().strip() = "ABCD"
print(len(str)) => 4
print(str[-1]) => "D"


8. 리스트와 내장함수 (1)

리스트 - 파이썬의 배열. 내부적으로 연결리스트 방식을 채택하고있음.


-> 리스트 선언법
a = [1,2,3] // [1,2,3]
b = list() // []


a = [1,2,3,4]
b = list(range(1,10))
c = a + b
print(c) // a와 b가 합쳐짐 미친문법

* 파이썬에서는 음수 인덱스도 지원함 -> 리스트가 비어있으면 사용불가 + 아웃오브레인지여도 사용 불가
a[-2] // 3


* 내장 함수

변수명.append()	리스트에 원소 삽입	| O(1)
변수명.sort()	오름차순으로 정렬	| O(NlogN)
변수명.sort(reverse=True)	내림차순으로 정렬	| O(NlogN)
변수명.reverse()	원래 원소의 순서를 뒤집어 놓음 | O(N) -> arr[::-1] 도 가능
변수명.insert(인덱스, 삽입할 값)	지정한 위치에 원소 삽입 | O(N)
변수명.count(특정 값)	특정한 값을 가지는 데이터의 개수	| O(N)
변수명.remove(특정 값)	특정한 값을 갖는 원소 제거	| O(N)


1) 리스트에 원소 추가 - arr.append(원소)
-> 반환 값 없음
-> side effect o
-> 제일 뒤에 추가됨

2) 리스트의 특정 위치에 원소 추가 - arr.insert(인덱스, 원소)
-> 반환 값 없음
-> side effect o

3) 리스트의 특정 위치 원소를 제거 - arr.pop([,인덱스])
-> 반환 값 없음
-> side effect o
-> 빼낸 값을 활용 가능(변수 할당하여)
-> 인덱스 안 쓰면 리스트의 맨 뒤 원소 제거

4) 리스트의 특정 원소 제거 - arr.remove(리스트에 존재하는 원소)
-> 반환 값 없음
-> side effect o

5) 리스트의 특정 원소 인덱스 알기 - arr.index(리스트에 존재하는 원소)
-> 반환 값 없음
-> side effect o

6) 리스트 요소 모두 더하기 - sum(arr)
-> side effect x
-> 정수형 리스트만 가능한듯

7) 리스트 요소 중 최댓값 구하기 - max(arr)
-> side effect x

8) 리스트 요소 중 최솟값 구하기 - min(arr)
-> side effect x
-> min(1,2,3) // 1 - 인자값 중 최솟값


* import random as r // 랜덤 모듈 임포트 - 'r'로 사용하면 됨

a = list(range(1, 11))
r.shuffle(a) // 무작위 리스트 요소 출력


9) 리스트 정렬 - arr.sort([,reverse])
-> side effect o **

a.sort() // 오름차순
a.sort(reverse=True) // 내림차순


** 주의
print(a.sort()) // 하면 안되네

a.sort()
print(a) // 이렇게 해야 되네 -> 반환값이 없기 때문


10) 리스트 초기화(모든 요소 삭제) - arr.clear()
-> side effect o


* 10.5) 리스트 특정 요소 모두 삭제

arr = [1, 2, 3, 4, 4, 5]
remove_set = {3, 4} // set 뿐 아니라 리스트, 튜플도 되는듯?

result =[x for x in arr if x not in remove_set]




9. 리스트와 내장함수 (2)

1) 리스트 슬라이스 - arr[[,숫자1]:숫자2]
-> side effect x
-> 문자열과 같음

2) 리스트의 길이 - len(arr)
-> side effect x
-> 문자열과 같음

3) 리스트 합치기 - arr.extend(arr2)



* for문과 리스트의 활용

a = [11, 12, 35, 21, 36, 90]

for x in a: // 문자열과 같음 인덱스가 아닌 원소로 접근
    print(x, end=" ")

for i in range(len(a)): // 문자열과 같음
    print(a[i], end=" ")

for x in enumerate(a): // 원소를 튜플 형태로 출력 (x가 튜플임)
    print(x)

(0, 11) // (인덱스, 원소값)
(1, 12)
(2, 35)
(3, 21)
(4, 36)
(5, 90)



* Tuple
그래프 알고리즘 구현시 자주 사용

다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에서는 우선순위 큐를 이용하는데 해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변경되지 않는다. 그래서 그 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다.
또한, 튜플은 리스트에 비해 상대적으로 공간 효율적이고, 일반적으로 각 원소의 성질이 서로 다를 때 사용한다.
흔히 다익스트라 최단 경로 알고리즘에서는 '비용'과 '노드 번호'라는 서로 다른 성질의 데이터를 (비용, 노드번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다.



a = (1,2,3,4,5)
print(a) // (1, 2, 3, 4, 5)
print(a[4]) // 5

** 리스트와 유사하나 튜플은 값을 변경할 수 없다

a[0] = 10 // error


a = [11, 12, 35, 21, 36, 90]
for x in enumerate(a): // tuple로 변경
    print(x[0], x[1]) // 0 11 1 12 2 35 3 21 4 36 5 90

for i, v in enumerate(a): // 더 자주 쓰이는 방법
    print(i, v)

a = (1, 2, 3, 4)
b, c, d, e = a // 비구조화할당


* 만약 any 를 생각하지 못하고 tuple 배열의 맥스를 구해야한다면 ?
-> 튜플을 (인덱스, 값)이 아닌 (값, 인덱스) 한 다음에 max(tuple[0])이렇게 하면 된다. max(튜플) 하면은 무조건 인덱스 0인 요소만 비교하기 때문



* all 함수 - 리스트에 조건걸 때 유용

all or any (조건문;반복문)

if all(100 > x for x in a): // 리스트의 모든 요소가 조건을 만족할 때
    print("모든 리스트 요소가 만족합니다.")
else:
    print("하나라도 만족 못하면 이리 옵니다.")

* any 함수 - 하나라도 만족할 떄

if any(100 > x for x in a):
    print("하나라도 만족합니다.")
else:
    print("모두 만족 못하면 이리 옵니다.")




10. 2차원 리스트 생성과 접근

* 리스트컴프리헨션
리스트를 생성하는 컴프리헨션을 리스트컴프리헨션 이라고 부릅니다.

a = [x for x in range(10)]
b = [1 for _ in range(10)]
c = [list(range(3)) for _ in range(3)]
d = [i for i in range(20) if i % 2 == 1]
e = [ 2 * x for x in range(1, 10 + 1) ]
e2 = [ x for x in range(10) if x < 5 if x % 2 == 0 ]
f = [ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
g = [ (x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달 시키기', '가서 먹기']]

ss = [(x, y) for x, y in enumerate(arr)] // 이런식으로 튜플 배열 생성 가능



a = [0] * 10 // 미친문법
print(a) // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a = [[0] * 3 for _ in range(3)] // 이차원 리스트를 초기화 시킬때는 무조건 리스트 컴프리헨션 이용해야 함
print(a) // [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in a: // 자주 사용되는 2차원 리스트 출력법(행렬처럼)
    print(i)

for i in a: // 위 코드를 세분화
    for j in i:
        print(j, end=" ")
    print()



11. Set 자료형

-> 집합에 관련된 것을 쉽게 처리하기 위해 만들어진 자료형

* 중복을 허용하지 않는다.
* 순서가 없다(Unordered).

s1 = set([1,2,3])
s2 = {'a','b','c'}
s3 = set("hello")
print(s1) // {1, 2, 3}
print(s2) // {'a', 'b', 'c'}
print(s3) // {'o', 'l', 'e', 'h'}




리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만 set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없다.

만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한후 해야 한다.

arr = [11, 11, 11, 23, 412, 3, 5123, 123, 3, 123, 1, 23, 1]
s1 = set(arr)
arr2 = list(s1)
print(arr2) // [1, 3, 5123, 11, 23, 123, 412]


※ 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.
* set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.
*** 또한 '특정한 데이터가 이미 등장한 적이 있는지 여부를 체크'할 때 매우 효과적


& : 교집합
| : 합집합
- : 차집합

-> 모두 Set형태로 출력

* 관련 메서드

1) 값 1개 추가하기 - add O(1)
2) 값 여러개 추가하기 - update
3) 특정 값 제거하기 - remove O(1)

s1 = set([11,11,2,3,3,4])

s1.add(1)
s1.update([4,5,6])
s1.remove(11)

print(s1) // {1, 2, 3, 4, 5, 6}





12. 딕셔너리 자료형

자바스크립트 객체와 비슷

-> 내부적으로 해시테이블 이용. 데이터 검색 및 수정이 o(1) 복잡도를 가짐. 리스트보다 훨씬 빠르게 동작함 + 공간 효율적

*
딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. 이것이 바로 딕셔너리의 가장 큰 특징이다. baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a = {1: 'hi'}
a = { 'a': [1,2,3]}


* 딕셔너리 쌍 추가, 삭제하기

dic[key] = value // 추가
del dic[key] // 삭제


a = {1: 'a'}
>>> a[3] = 'b' // 키가 숫자
>>> a
{1: 'a', 3: 'b'}

a['name'] = 'pey' // 키가 문자열
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}

dic = {"1": "a", "2": "b"}
del dic["1"] // 삭제

-> 동일한 키, 값 쌍을 넣으면 먼저 있던 것이 사라짐



* 딕셔너리 관련 함수들

1) key값 반환 - keys()

dic = {"1": "a", "2": "b"}

print(dic.keys()) // 디폴트로 dict_keys 객체 반환
print(list(dic.keys())) // 리스트로 변환도 가능

for i in dic.keys(): // 그냥 리스트와 같다고 생각해도 되나 리스트의 메서드는 사용할 수 없음
    print(i)

for i in list(dic.keys()):
    print(i)


2) value값 반환 - values()

key와 마찬가지


dic = {"1": "a", "2": "b"}

print(dic.values())
print(list(dic.values()))

for i in dic.values():
    print(i)

for i in list(dic.values()):
    print(i)




3) 키, 값 쌍 얻기 - items()

items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다. dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다.

dic = {"1": "a", "2": "b"}
print(dic.items()) // dict_items([('1', 'a'), ('2', 'b')])
print(list(dic.items())) // [('1', 'a'), ('2', 'b')]


4) 딕셔너리 비우기 - clear()


dic = {"1": "a", "2": "b"}
dic.clear() // sort와 마찬가지로 print() 내부에서 사용 x 반환값이 없기떄문
print(dic) // {}


5) key로 value 얻기 - get() ***

dic = {"1": "a", "2": "b"}
print(dic.get("1"))
print(dic.get("1", 0)) => key에 해당하는 값이 없으면 디폴트 값 가져옴
-> 직접 접근과 다르게 키값이 딕셔너리 내부에 존재하지 않아도 오류 출력하지 않음

    ***** 테크닉
  for x in arr1:
    d[x] = d.get(x, 0) + 1
  for x in arr2:
    d[x] = d.get(x, 0) - 1

6) 해당 key가 딕셔너리 안에 있는지 조사하기 - in

dic = {"1": "a", "2": "b"}

print('1' in dic) // True




13. 함수 만들기

1)
def add(a,b):
    return a+b

print(add(1,2))

2) 미친문법 리턴 두 개 이상 가능
def solution(a, b):
    c = a + b
    d = a - b
    return c, d


a1, a2 = solution(10, 2)
print(a1, a2) // 12, 8
print(solution(8, 4)) // (12, 4) 튜플 형태로 출력


3) 소수 판별하기

a = [12, 13, 7, 9, 19, 11, 14, 6, 5, 3, 21, 100, 101]

def sol(arr):
    result = []
    for i in arr:
        for x in range(2, i):
            if i % x == 0:
                break
            if x == i - 1:
                result.append(i)
    return result


re = sol(a)
re.sort()
print(re) // [3, 5, 7, 11, 13, 19, 101]





14. 람다 함수

-> 익명 함수, 람다 표현식

a = lambda x: x + 2 // x : 매개변수 x + 2 : 리턴값
print(a(3)) // 5


**** 람다 표현식이 유용할 때?
-> 어떤 함수의 매개 표현식으로 들어갈 때 ex) map 함수, sort 함수 내부에도 사용 가능


a = [1, 2, 3, 4]

def plus_one(x):
    return x + 1

print(list(map(plus_one, a)))
print(list(map(lambda x: x + 1, a))) // 매우 유용


** tuple sorting (x, y) 형태일 때

tuple.sort() -> x 기준으로 정렬되고 x가 같을 경우 y 기준 정렬
tuple.sort(key=lambda v: (v[1], v[0])) -> y 기준으로 정렬되고 y가 같을 경우 x 기준으로 정렬
arr.sort(key=lambda v: v[0]) -> x기준으로만 정렬. y는 입력된 순서 그대로
tuple.sort(key=lambda v: (v[0], -v[1])) -> x 기준으로 정렬되고 x가 같을 경우 y는 내림차순 정렬

15. 기타 내장 함수

1) eval() - 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환

result = eval("3*5")
print(result) // 15


2) sorted() - 이터러블 객체가 들어왔을 때 정렬된 결과를 리스트로 반환.
=> 주로 "리스트"가 아닌 이터러블 객체에 사용하는듯 리스트는 그냥 sort() 쓰면 된다.

result = sorted([1, 2, 3])
result2 = sorted("asdb")
result3 = sorted((1, 2, 3), reverse=True)
result4 = sorted({"!":1,"2":3})

print(result)
print(result2)
print(result3)
print(result4)

result6 = sorted([("홍길동", 60), ("강감찬", 80), ("이순신", 30)],
 key=lambda x: x[1], reverse=True)
print(result6) // [('강감찬', 80), ('홍길동', 60), ('이순신', 30)]

result6.sort(key=lambda x: x[1]) // 이것도 가능
print(result6)

-> 이차원 리스트나 튜플 배열일 때 이렇게 할 수 있음. 딕셔너리나 셋은 안되나봐

* key - 어떤 원소 기준으로 정렬할 것인지?
* lambda - 정렬 기준은?(함수)







```
