import copy
from collections import deque


def sol():
    global max_cnt
    # 시계방향
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    # 카페 개수 세기
    def counting(arr):
        global max_cnt
        s = set(arr)
        if len(s) > max_cnt:
            max_cnt = len(s)

    def dfs(L, x, y, d, visited):
        for s in range(d, 4):
            nx = x + dx[s]
            ny = y + dy[s]
            # 사이클 형성 & 중복된 카페 체크
            if nx == i and ny == j:
                # 길이 2짜리 사이클 제외
                if len(visited) == 2:
                    return
                flag = True
                for p in range(len(visited)):
                    for q in range(p+1, len(visited)):
                        if visited[p] == visited[q]:
                            flag = False
                if flag:
                    counting(visited)
                return

            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and check[nx][ny] == 0:
                check[nx][ny] = 1
                visited.append(grid[nx][ny])
                dfs(L + 1, nx, ny, s, visited)
                check[nx][ny] = 0
                visited.pop()

    t = int(input())

    for test_case in range(1, t+1):
        max_cnt = 0
        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                check = [[0]*n for _ in range(n)]
                check[i][j] = 1
                visited = [grid[i][j]]
                dfs(0, i, j, 0, visited)
        if max_cnt == 0:
            print("#%d %d" % (test_case, -1))
        else:
            print("#%d %d" % (test_case, max_cnt))


sol()
