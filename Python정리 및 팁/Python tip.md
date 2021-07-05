# math 라이브러리

```py
import math

1) 제곱근 구하기 math.sqrt(4)

2) 거듭제곱 구하기 math.pow(1,2) -> x**y 가 좀 더 편하고 나은듯

3) 천장값, 바닥값 math.ceil(x), math.floor(x)

4) 최대공약수 math.gcd(a,b)
```

# 내장함수 zip

```py

zip 함수를 이용하면 pair하게 로직 처리 가능 -> enumerate 랑 약간 비슷한듯

arr1 = [1,2,3,4]
arr2 = [1,2,3,4,5,6,7,8,9]

for a1,a2 in zip(arr1, arr2):
  print(a1,a2)

for pair in zip(arr1, arr2):
  print(pair)

# 결과
1 1
2 2
3 3
4 4
(1, 1)
(2, 2)
(3, 3)
(4, 4)


```

# 전치행렬 경우의수 구하는 법

```py

arr = [[1, 2, 3, 4],
       [7, 8, 9, 10],
       [13, 14, 15, 16]]

candi = []
for i in range(1, len(arr) + 1):
  for tmp in it.combinations(range(len(arr[0])), i):
    candi.append(tmp)

for cand in candi:
  tmp = [[a[key] for key in cand] for a in arr]
  print(tmp)

```

# 리스트 다루기 시리즈

## 리스트 다루기1 (이차원 배열 일부 빼내기)

```py
arr = [
  [1,2,3,4,5],
  [5,6,7,8,9],
  [9,10,11,12,13],
  [14,15,16,17,18]
]

n,m = 3,2 # 행,열
for i in range(len(arr)-n+1):
  for j in range(len(arr[0])-m+1):
    res = [row[j:j+m] for row in arr[i:i+n]] # row 먼저 뽑고 거기서 col 뽑는다.
    for r in res:
      print(r)
    print()
```

## 리스트 다루기2 (이차원 배열 90도 회전 시키기)

```py
arr = [
  [1,2,3],
  [6,7,8],
  [11,12,13],
]
row_len,col_len = len(arr), len(arr[0])
result = [[0]*col_len for _ in range(row_len)]
for i in range(row_len):
  for j in range(col_len):
    result[j][row_len-i-1] = arr[i][j]

for r in result:
  print(r)


```

## 리스트 다루기3 (이차원 배열 세로로 좌표이동)

## 리스트 다루기4 (이차원 배열 복사)

## 리스트 다루기5 (이차원 배열 소용돌이 이동)

## 리스트 다루기6 (이차원 배열 외곽이동)

## 리스트 다루기7 (이차원 배열 떨어뜨리기)

# 문자열 다루기 시리즈

## 문자열 다루기1 (replace)

```py
# 활용
def shap_to_lower(s):
    s = s.replace('C#', 'c').replace('D#', 'd').replace(
        'F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return s

```

## 문자열 다루기2 (슬라이스)

```py

s = "abcde"
s[::-1] # edcba
s[:-3] # ab
s[-3:] # cde
s[::2] # ace

```
