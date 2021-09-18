# 골드3 - 학교탐방하기
# MST

# 최소스패닝트리, 최대스패닝트리 구하면 된다.

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
edges = []

for _ in range(m+1):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

worst = sorted(edges)[:]
best = sorted(edges, key=lambda x: (-x[0], x[1], x[2]))[:]


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


max_val = 0
min_val = 0
up_cnt = 0

for edge in worst:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        if cost == 0:
            up_cnt += 1
        union_parent(parent, a, b)

max_val += up_cnt ** 2

for i in range(n+1):
    parent[i] = i

up_cnt = 0
for edge in best:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        if cost == 0:
            up_cnt += 1
        union_parent(parent, a, b)

min_val += up_cnt ** 2

print(max_val - min_val)
