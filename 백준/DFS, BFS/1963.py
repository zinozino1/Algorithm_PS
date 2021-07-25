# 골드4 - 소수 경로
# 에라토스테네스의 체 + BFS

# 에라토스 테네스의 체를 적용하지 않았을 경우 TLE

from collections import deque

T = int(input())


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return sieve


primes = prime_list(10000)


def bfs(v):
    check = [0] * 10000
    check[v] = 1
    q = deque()
    q.append(v)
    level = 0
    while q:
        for _ in range(len(q)):
            nv = list(str(q.popleft()))
            if int("".join(nv)) == e:
                return level

            for k in range(3, -1, -1):
                prev = nv[k]
                for l in range(10):
                    if k == 0 and l == 0:
                        continue
                    nv[k] = str(l)
                    if primes[int("".join(nv))] and check[int("".join(nv))] == 0:
                        check[int("".join(nv))] = 1
                        q.append(int("".join(nv)))
                    nv[k] = prev

        level += 1
    return "Impossible"


for _ in range(T):
    s, e = map(int, input().split())
    print(bfs(s))
