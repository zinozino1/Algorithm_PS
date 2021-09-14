# 골드5 - 회장 뽑기
# 플로이드 워셜


# 플로이드 응용문제 :  각 후보자들의 최소 거리를 구하는 게 핵심이고
# 나머진 플로이드 응용

n = int(input())
order = []

while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    order.append((s, e))
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for od in order:
    s, e = od
    graph[s][e] = 1
    graph[e][s] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

min_score = 1e9
for g in graph[1:]:
    min_score = min(min_score, max(g[1:]))

candidate = []
for i, g in enumerate(graph[1:]):
    if max(g[1:]) == min_score:
        candidate.append(i+1)

print(min_score, len(candidate))
print(*candidate)
