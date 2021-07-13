# 실버3-바이러스

# DFS 풀이
from collections import deque
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (n+1)


def dfs(v):
    visited[v] = 1
    for next in adj[v]:
        if visited[next] == 0:
            dfs(next)


dfs(1)
print(visited.count(1)-1)

# BFS 풀이

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (n+1)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for next in adj[curr]:
                if visited[next] == 0:
                    visited[next] = 1
                    q.append(next)


bfs(1)
print(visited.count(1)-1)
