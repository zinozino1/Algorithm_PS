import copy
from collections import deque


def sol():
    # 가용 가능한 집 수 & 점수 구하기
    def cal():
        score = 0
        cnt = 0
        for p in range(n):
            for q in range(n):
                if check[p][q] == 1 and tmp_grid[p][q] == 1:
                    cnt += 1
        score = cnt*m
        return score, cnt

    # BFS
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        cnt = 0

        while q:
            if cnt == k-1:
                break
            for _ in range(len(q)):
                curr = q.popleft()

                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        q.append((nx, ny))
            cnt += 1
        s, c = cal()
        return s, c

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    t = int(input())
    test_case = 1
    for _ in range(t):
        max_cnt = -1e9
        n, m = map(int, input().split())
        grid = []

        t_home = 0
        for _ in range(n):
            temp = list(map(int, input().split(' ')))
            grid.append(temp)
            for i in range(n):
                if temp[i] == 1:
                    t_home += 1
        k = 1

        # 커버할 수 있는 k까지 돌림 -> 시간 줄이기
        while t_home*m-(k*k+(k-1)*(k-1)) >= 0:
            for i in range(n):
                for j in range(n):
                    tmp_grid = copy.deepcopy(grid)
                    check = [[0] * n for _ in range(n)]
                    check[i][j] = 1
                    s, c = bfs(i, j)

                    if k*k+(k-1)*(k-1) <= s:
                        if c > max_cnt:
                            max_cnt = c
            k += 1

        print("#%d %d" % (test_case, max_cnt))
        test_case += 1


sol()
