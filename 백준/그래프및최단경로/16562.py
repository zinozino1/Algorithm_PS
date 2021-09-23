# 골드3-친구비
# 유니온파인드

n, m, k = map(int, input().split())
friend_cost = list(map(int, input().split()))
friend_cost.insert(0, 0)
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    cost = min(friend_cost[a], friend_cost[b])

    if a < b:
        parent[b] = a
        friend_cost[a] = cost
    else:
        parent[a] = b
        friend_cost[b] = cost


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


for _ in range(m):
    s, e = map(int, input().split())
    union_parent(parent, s, e)

for i in range(1, n+1):
    find_parent(parent, i)

tmp = []
for i in range(1, n+1):
    tmp.append((parent[i], friend_cost[i]))
tmp.sort()
curr = tmp[0][0]
res = tmp[0][1]

for i in range(n):
    if tmp[i][0] != curr:
        res += tmp[i][1]
        curr = tmp[i][0]

if res <= k:
    print(res)
else:
    print("Oh no")
