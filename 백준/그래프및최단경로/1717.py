# 골드4 - 집합의 표현
# 유니온 파인드

# 유니온 파인드 기본형 문제


import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


for _ in range(m):
    opt, a, b = map(int, input().split())
    if opt == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
