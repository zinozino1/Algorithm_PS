# 골드4 - 소수의 연속합
# 투포인터

# 투포인터 기본형
# rt, lt 값에 따른 종료조건 형식 기억하기

n = int(input())

tmp = [1]*(n+1)
for i in range(2, n+1):
    if tmp[i] == 1:
        for j in range(i+i, n+1, i):
            tmp[j] = 0

primes = []
for i in range(2, len(tmp)):
    if tmp[i] == 1:
        primes.append(i)

lt = 0
rt = 0
tot = 0
cnt = 0
while True:
    if tot == n:
        cnt += 1
        tot -= primes[lt]
        lt += 1
    elif tot < n:
        if rt > len(primes)-1:
            break
        tot += primes[rt]
        rt += 1
    elif tot > n:
        if lt > len(primes)-1:
            break
        tot -= primes[lt]
        lt += 1

print(cnt)
