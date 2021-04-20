# 골드5-연구소
# BFS, DFS 활용
# 조합구할 때 itertools 고려해보기 -> 코드 훨씬 짧아짐
# for tmp in it.combinations(arr, k) => arr은 1차원 배열, k는 뽑는 가지수


import copy
from collections import deque
import itertools as it


def sol():
    global max_cnt

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    def bfs(arr, tmp_grid):
        global max_cnt
        q = deque()
        check2 = [[0] * m for _ in range(n)]
        # BFS 시작 방향이 여러개일 수 있으므로 큐에 시작 지점 다 넣어줌
        for v in arr:
            q.append(v)
            check2[v[0]][v[1]] = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                tmp_grid[curr[0]][curr[1]] = -1
                for s in range(4):
                    nx = curr[0] + dx[s]
                    ny = curr[1] + dy[s]
                    if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and check2[nx][ny] == 0 and \
                            tmp_grid[nx][ny] == 0:
                        check2[nx][ny] = 1
                        q.append((nx, ny))
        score = 0
        for g in tmp_grid:
            score += g.count(0)
        if score > max_cnt:
            max_cnt = score

    def dfs(L, a):
        if L == 3:
            # DFS 트리마다 배열 복사할 필요는 없음 DFS 트리 순회 종료 후 BFS에만 배열 복사해주면 된다
            # 복사 안해주면 다른 grid 배열에도 영향을 미치게 때문에 복사해줘야함
            tmp_grid = [layer[:] for layer in grid]
            virus = []
            for p in range(n):
                for q in range(m):
                    if tmp_grid[p][q] == 2:
                        virus.append((p, q))
            bfs(virus, tmp_grid)
            return

        else:
            # 벽 세울 수 있는 공간 중에서 3개 좌표 뽑는 조합
            for s in range(a, len(empty_space)):
                grid[empty_space[s][0]][empty_space[s][1]] = 1
                dfs(L + 1, s + 1)
                grid[empty_space[s][0]][empty_space[s][1]] = 0

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = -1e9

    empty_space = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                empty_space.append((i, j))

    dfs(0, 0)

    print(max_cnt)


sol()
