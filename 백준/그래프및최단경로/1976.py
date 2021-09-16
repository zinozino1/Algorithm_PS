# 골드4 - 여행가자
# 유니온 파인드

# 여행경로 존재 여부를 찾는것은 모든 여행지가 같은집합인 것을 판단하는 로직과 같다.
# 플로이드 워셜로도 풀이가 가능한듯함


n = int(input())
m = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
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


for i, info in enumerate(infos):
    for j in range(len(info)):
        if info[j] == 1:
            union_parent(parent, i+1, j+1)

check = set()
for p in plan:
    check.add(find_parent(parent, p))
if len(check) == 1:
    print("YES")
else:
    print("NO")


# 플로이드 워셜 풀이

n = int(input())  # 총 도시의 수
m = int(input())  # 여행 계획에 속한 도시들의 수
graph = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))

# 플로이드-워셜 알고리즘을 통해 모든 노드 간의 최소 거리를 구한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and i != j:  # 길이 없다는 뜻
            graph[i][j] = 1e9  # 10억으로 대입

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 여행 여부 확인
flag = True
pre_index = move[0] - 1
for i in range(1, m):
    if graph[pre_index][move[i] - 1] >= 1e9:  # 길이 없는 경우
        flag = False
        break
    else:
        pre_index = move[i] - 1

if flag:
    print("YES")
else:
    print("NO")
