# 골드4 - 플로이드
# 플로이드 워셜

# 기본형태

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = min(graph[s][e], c)  # 기존 거리보다 짧은 것이 있다면 갱신

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == int(1e9):
            print(0)
        else:
            print(graph[i][j], end=" ")
    print()
