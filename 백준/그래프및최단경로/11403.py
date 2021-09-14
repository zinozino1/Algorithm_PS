# 실버1 - 경로찾기
# 플로이드 워셜

# 최단거리가 아닌 갈 수 있는지 없는지 여부를 확인한다.

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
