# 실버1-숨바꼭질
# BFS는 큐에서 뺼 때가 아니라 넣을 때 방문표시를 해줘야 중복 방문이 일어나지 않는다.

from collections import deque

n, k = map(int, input().split())
ctx = [1, -1, 2]


def bfs(pos):

    q = deque()
    q.append(pos)
    time = 0
    visited = [0]*100001
    visited[n] = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == k:
                return time
            for s in range(3):
                if s == 2 and 0 <= curr*ctx[2] < 100001 and visited[curr*ctx[2]] == 0:
                    q.append(curr*ctx[2])
                    visited[curr*ctx[2]] = 1
                elif (s == 0 or s == 1) and 100001 > curr + ctx[s] >= 0 and visited[curr + ctx[s]] == 0:
                    q.append(curr+ctx[s])
                    visited[curr+ctx[s]] = 1

        time += 1


print(bfs(n))
