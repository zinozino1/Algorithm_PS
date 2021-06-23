1. math 라이브러리

```py
import math

1) 제곱근 구하기 math.sqrt(4)

2) 거듭제곱 구하기 math.pow(1,2) -> x**y 가 좀 더 편하고 나은듯

3) 천장값, 바닥값 math.ceil(x), math.floor(x)

4) 최대공약수 math.gcd(a,b)
```

2. 내장함수 zip

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
