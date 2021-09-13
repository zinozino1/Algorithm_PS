# 골드3 - 파티
# 다익스트라

# 다익스트라 응용. 시작점과 도착지 각각에서 다익스트라 돌려주면 된다.

import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))  # 도착 노드, 가중치


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, curr = heapq.heappop(heap)
        if distance[curr] < dist:
            continue

        for nxt in graph[curr]:
            next_dist = dist + nxt[1]  # 시작 노드로부터의 거리
            if next_dist < distance[nxt[0]]:
                distance[nxt[0]] = next_dist
                heapq.heappush(heap, (next_dist, nxt[0]))


res = -1e9
for i in range(1, n+1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    go = distance[x]
    distance = [INF] * (n + 1)
    dijkstra(x)
    back = distance[i]
    res = max(go+back, res)

print(res)
