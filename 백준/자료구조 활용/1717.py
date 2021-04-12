# 골드4-유니온파인드-집합의 표현
# Union-Find
import sys

input = sys.stdin.readline


def get_parent(x):
    if parent[x] == x:
        return x
    p = get_parent(parent[x])
    parent[x] = p
    return p

# 합집합 만들기


def union(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if x != y:
        parent[y] = x


def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])


n, m = map(int, input().split())
parent = {}

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    z, x, y = map(int, input().split())

    if not z:
        union(x, y)

    if z:
        # 부모가 같으면 같은집합임
        if find_parent(x) == find_parent(y):
            print('YES')
        else:
            print('NO')
