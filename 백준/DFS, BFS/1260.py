# 실버2-DFS와 BFS


from collections import deque
n, m, init = map(int, input().split())

adj = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
for i in range(len(adj)):
    adj[i].sort()

visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
res_dfs = []
res_bfs = []


def dfs(v):
    visited_dfs[v] = 1
    res_dfs.append(v)
    for next in adj[v]:
        if visited_dfs[next] == 0:
            dfs(next)


def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            res_bfs.append(curr)
            for next in adj[curr]:
                if visited_bfs[next] == 0:
                    visited_bfs[next] = 1
                    q.append(next)


dfs(init)
print(*res_dfs)
bfs(init)
print(*res_bfs)
