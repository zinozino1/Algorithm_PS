# 골드5 - 선수과목
# 위상정렬

# for _ in range(len(curr)) -> 큐의 레벨마다 작업 수행

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    degree[e] += 1

res = [0] * (n+1)


def topologySort():
    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)

    level = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()

            res[curr] = level
            for nxt in graph[curr]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        level += 1


topologySort()

print(*res[1:])
