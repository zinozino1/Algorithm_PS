# 골드5 - 호석이 두마리 치킨
# BFS+DFS 응용문제

# 조합은 DFS로 찾고 최단경로는 BFS로 조진다

from collections import deque
import itertools as it

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def find_shortest_path(v):
    q = deque()
    q.append(v)
    check = []
    lv = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for nxt in graph[curr]:
                if nxt not in check:
                    if nxt in tmp:
                        return lv*2
                    check.append(nxt)
                    q.append(nxt)
        lv += 1


comp = 1e9
chicken = []
for tmp in it.combinations(range(1, n+1), 2):
    tot_dis = 0
    for i in range(1, n+1):
        if i in tmp:
            continue
        tot_dis += find_shortest_path(i)

    if tot_dis < comp:
        comp = tot_dis
        chicken.append((tmp[0], tmp[1], tot_dis))

chicken.sort(key=lambda x: (x[2], x[0], x[1]))
print(*chicken[0])
