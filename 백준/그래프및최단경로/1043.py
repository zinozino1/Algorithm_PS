# 골드4 - 거짓말
# 유니온 파인드

# 유니온 파인드 활용문제


n, m = map(int, input().split())
tmp = list(map(int, input().split()))
truth_num, thruth_people = tmp[0], tmp[1:]

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


partys = []

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    if len(party) > 1:
        for i in range(len(party)-1):
            union_parent(parent, party[i], party[i+1])
    partys.append(tuple(party))

enable_cnt = 0
for party in partys:
    flag = True
    for j in range(len(party)):
        parent_num = find_parent(parent, party[j])
        parent_set = [i for i in range(
            1, n+1) if parent_num == find_parent(parent, parent[i])]

        for ps in parent_set:
            if ps in thruth_people:
                flag = False
    if flag:
        enable_cnt += 1

print(enable_cnt)
