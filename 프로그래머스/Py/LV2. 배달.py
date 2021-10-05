# 플로이드 워셜

# O(n^3)

def solution(N, road, K):
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for r in road:
        s, e, c = r
        if graph[s][e] != int(1e9):
            graph[s][e] = min(graph[s][e], c)
        else:
            graph[s][e] = c
        if graph[e][s] != int(1e9):
            graph[e][s] = min(graph[e][s], c)
        else:
            graph[e][s] = c

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0

    for s in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][s] + graph[s][j])

    res = 0

    for g in graph[1][1:]:
        if g <= K:
            res += 1
    return res
