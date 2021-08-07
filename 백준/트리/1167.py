# 골드3 - 트리의 지름
# 트리

# 1967과 동일

# DFS 이용 풀이
import heapq
from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    target = list(map(int, input().split()))
    node = target[0]

    for i in range(1, len(target), 2):
        if target[i] == -1:
            break
        tree[node].append((target[i], target[i+1]))

maxLen = -1e9
next_node = -1
res = -1e9


def dfs(v, tot, flag):
    global maxLen, next_node, res
    visited[v] = 1
    for ne in tree[v]:
        if visited[ne[0]] == 1 and len(tree[v]) == 1:
            if tot > maxLen:
                maxLen = tot
                next_node = v
            if flag:
                res = max(res, tot)
        if visited[ne[0]] == 0:
            dfs(ne[0], tot+ne[1], flag)


visited = [0]*(n+1)
dfs(1, 0, False)
visited = [0]*(n+1)
dfs(next_node, 0, True)
print(res)


# BFS 이용 풀이


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    target = list(map(int, input().split()))
    node = target[0]

    for i in range(1, len(target), 2):
        if target[i] == -1:
            break
        tree[node].append((target[i], target[i+1]))

maxLen = -1e9
res = -1e9


def bfs(v):
    q = deque()
    q.append((v, 0))
    visited[v] = 1
    heap = []
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            heapq.heappush(heap, (-curr[1], curr[1], curr[0]))
            for ne in tree[curr[0]]:
                if visited[ne[0]] == 0:
                    q.append((ne[0], curr[1]+ne[1]))
                    visited[ne[0]] = 1
    if flag:
        return heapq.heappop(heap)[1]
    else:
        return heapq.heappop(heap)[2]


visited = [0]*(n+1)
flag = False
next_node = bfs(1)
visited = [0]*(n+1)
flag = True
print(bfs(next_node))
