# 골드5 - 최소비용구하기
# 다익스트라

# 다익스트라 기본

import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))  # 도착노드, 비용
A, B = map(int, input().split())


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))  # 비용, 노드

    while heap:
        dist, curr = heapq.heappop(heap)  # 현재노드와 시작노드의 거리, 현재 노드
        if distance[curr] < dist:
            continue  # 이미 방문한 노드

        for nxt in graph[curr]:
            next_cost = dist + nxt[1]
            if distance[nxt[0]] > next_cost:
                distance[nxt[0]] = next_cost
                heapq.heappush(heap, (next_cost, nxt[0]))  # 시작노드로부터의 거리, 현재 노드


dijkstra(A)
print(distance[B])
