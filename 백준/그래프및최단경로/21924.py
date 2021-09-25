# 골드4 - 도시건설
# MST

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
edges = []
tot = 0
for _ in range(m):
    s, e, c = map(int, input().split())
    edges.append((c, s, e))
    tot += c
edges.sort()


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


res = 0

for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        res += cost
for i in range(1, n+1):
    find_parent(parent, i)

if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(tot-res)
