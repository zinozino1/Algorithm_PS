# 골드4 - 네트워크
# 크루스칼

# MST 기본

n = int(input())
m = int(input())
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


edges = []
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))
edges.sort()

res = 0
for edge in edges:
    cost, v1, v2 = edge
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        res += cost

print(res)
