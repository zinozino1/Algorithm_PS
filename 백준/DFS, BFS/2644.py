# 실버2-촌수계산
# 최단거리계산 - BFS

from collections import deque

n = int(input())
ts, te = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0]*(n+1)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    dis = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == te:
                print(dis)
                return
            for next in adj[curr]:
                if visited[next] == 0:
                    visited[next] = 1
                    q.append(next)
        dis += 1
    print(-1)


bfs(ts)
