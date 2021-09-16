# 골드4 - 도시분할계획
# 크루스칼

# MST 구축하고 두 마을로 분할하려면 선택된 cost 하나씩 빼서 min값 갱신하면 된다.

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))

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


tmp_res = 0
costs = []
for edge in edges:
    cost, v1, v2 = edge
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        tmp_res += cost
        costs.append(cost)

res = 1e9
for c in costs:
    res = min(res, tmp_res-c)
print(res)
