# BFS인줄 알고 풀었으나 DFS였음
# BFS로 풀면 다른 등산로까지 침범하기때문에 불가능
# DFS로 송곳처럼 찔러야함


import copy
from collections import deque


def sol():
    global max_cnt

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 시작위치배열 반환
    def get_start_pos(arr):
        max_num = -1e9
        for tmp in arr:
            if max_num < max(tmp):
                max_num = max(tmp)
        start_pos = []
        for i in range(n):
            for j in range(n):
                if arr[i][j] == max_num:
                    start_pos.append((i, j))
        return start_pos

    # 4방향 탐색
    def dfs(L, x, y, tot):
        global max_cnt

        if L+1 > max_cnt:
            max_cnt = L+1
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and check[nx][ny] == 0 \
                    and grid[nx][ny] < grid[x][y]:
                dfs(L + 1, nx, ny, tot + 1)
                # break걸어줄 필요가 없다.

    t = int(input())

    for test_case in range(1, t+1):

        n, k = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]

        max_cnt = -1e9

        for i in range(n):
            for j in range(n):
                for q in range(k+1):
                    if grid[i][j] < 0:
                        grid[i][j] += q
                        continue

                    start_pos = get_start_pos(grid)
                    # 등산로 깎기
                    grid[i][j] -= q
                    for pos in start_pos:
                        check = [[0] * n for _ in range(n)]
                        check[pos[0]][pos[1]] = 1
                        dfs(0, pos[0], pos[1], 1)
                    # 원상복구
                    grid[i][j] += q

        print("#%d %d" % (test_case, max_cnt))


sol()
