# 골드3 - 서울 지하철 2호선
# 그래프

# 그래프 사이클과 최단 경로를 묻는 문제
# 사이클은 dfs로 찾는 것이 맞고, 최단경로까지 dfs로 하다가 TLE
# 최단 경로는 BFS를 돌리는 게 맞다

# find_cycle 부분 유심히 다시 보기 - 약간 비효율적이긴 한데 나한테 가장 잘 이해됨

from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
node = [[] for _ in range(n + 1)]
for _ in range(n):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)


def bfs(v):
    q = deque()
    q.append(v)
    check2 = [0]*(n+1)
    level = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in cycle:
                return level
            for ne in node[curr]:
                if check2[ne] == 0:
                    check2[ne] = 1
                    q.append(ne)
        level += 1


def traverse(v, dis):
    global min_dis
    if v in cycle:
        if dis < min_dis:
            min_dis = dis
    for ne in node[v]:
        if check[ne] == 0:
            check[ne] = 1
            traverse(ne, dis+1)
            check[ne] = 0


def find_cycle(v, prev):
    for ne in node[v]:
        if visited[ne] == 1 and prev != ne:
            idx = cycle.index(ne)
            s.add(tuple(sorted(cycle[idx:])))
            return
        else:
            if visited[ne] == 0:
                visited[ne] = 1
                cycle.append(ne)
                find_cycle(ne, v)
                visited[ne] = 0
                cycle.pop()


# cycle 찾기
s = set()
for k in range(1, n + 1):
    visited = [0] * (n + 1)
    if visited[k] == 0:
        visited[k] = 1
        cycle = [k]
        find_cycle(k, -1)
        break

cycle = list(s)[0]

# 최단거리 구하기
res = []
check = [0]*(n+1)
for i in range(1, n + 1):
    res.append(bfs(i))
print(*res)
