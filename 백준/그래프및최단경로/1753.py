# 골드5 - 최단경로
# 다익스트라


# 다익스트라 기본

import heapq

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
for _ in range(e):
    U, V, W = map(int, input().split())
    graph[U].append((V, W))
distance = [INF] * (v+1)


def dijkstra(start):
    # 초기화
    heap = []
    heapq.heappush(heap, (0, start))  # dist, now
    distance[start] = 0

    # 시작정점으로부터 최소 가중치 정점 구하기
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue

        # now 인접노드 가중치 업데이트
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(heap, (cost, nxt[0]))


dijkstra(start)

for i in range(1, v+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
