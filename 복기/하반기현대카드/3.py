# 3번 생화학 가스폭탄
# DFS or GCD 문제


# 완전탐색 + 체크 백트래킹 풀이-> 코드가 좀 지저분함


import math


def solution(l1, l2):
    check = set()
    check.add((0, 0))

    def dfs(L, a, b):
        for i in range(6):
            if i == 0:  # a 채우기
                na = l1
                if (na, b) not in check:
                    check.add((na, b))
                    dfs(L+1, na, b)
            elif i == 1:  # a 비우기
                na = 0
                if (na, b) not in check:
                    check.add((na, b))
                    dfs(L+1, na, b)
            elif i == 2:  # b 채우기
                nb = l2
                if (a, nb) not in check:
                    check.add((a, nb))
                    dfs(L + 1, a, nb)
            elif i == 3:  # b 비우기
                nb = 0
                if (a, nb) not in check:
                    check.add((a, nb))
                    dfs(L + 1, a, nb)
            elif i == 4:  # a->b
                if a+b > l2:
                    na = a-(l2-b)
                    nb = l2
                else:
                    nb = a+b
                    na = 0
                if (na, nb) not in check:
                    check.add((na, nb))
                    dfs(L+1, na, nb)
            elif i == 5:  # b->a
                if a+b > l1:
                    nb = b-(l1-a)
                    na = l1
                else:
                    na = a+b
                    nb = 0
                if (na, nb) not in check:
                    check.add((na, nb))
                    dfs(L+1, na, nb)

    dfs(0, 0, 0)
    res = set()
    for c in check:
        if c[0] != 0 and c[1] != 0:
            res.add(c[0])
            res.add(c[1])

    return sorted(list(res))


print(solution(2, 4))  # [2,4]
print(solution(5, 5))  # [5]
print(solution(3, 18))  # [3,6,9,12,18]
print(solution(10, 17))  # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(solution(5, 20))  # [5,10,15,20]


# GCD 풀이 -> 완벽..


def solution(l1, l2):
    gcd = math.gcd(l1, l2)
    maxN = max(l1, l2)
    res = list(range(gcd, maxN+gcd, gcd))
    return res


print(solution(2, 4))
print(solution(5, 5))
print(solution(3, 18))
print(solution(10, 17))
print(solution(5, 20))
