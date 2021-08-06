# 골드4-중량제한-이분탐색+BFS
# 중량을 이분탐색으로 결정하면서 가능한 경로 하나만 결정하면 된다.


import itertools as it
from collections import deque


def sol():

    def bfs(capa):
        # 간선 개수보다 1크게 만들어줌
        visited = [0]*(m+1)

        q = deque()
        q.append(start-1)
        visited[start-1] = 1

        while q:
            for _ in range(len(q)):
                x = q.popleft()
                # x와 연결된 노드들 검사
                for y, w in grid[x]:
                    # 방문하지 않았고, 중량보다 커야함
                    if visited[y] == 0:
                        if w >= capa:
                            q.append(y)
                            visited[y] = 1

        # 끝점에 도달하면 '가능한' 경로가 된다.
        if visited[end-1] == 1:
            return True
        else:
            return False

    n, m = map(int, input().split())
    grid = [[] for _ in range(n+1)]

    # 인접 리스트 정의 -> 메모리 절약 + 탐색 속도 상승
    for _ in range(m):
        x, y, w = map(int, input().split())
        grid[x-1].append((y-1, w))
        grid[y-1].append((x-1, w))

    start, end = map(int, input().split())

    lt = 1  # 최소 중량
    rt = 1000000000  # 최대 중량
    res = lt

    while lt <= rt:
        mid = (lt+rt) // 2

        # 가능한 경로가 있다면 중량 올리기
        if bfs(mid):
            res = mid
            lt = mid+1
        else:
            rt = mid-1

    print(res)


sol()
