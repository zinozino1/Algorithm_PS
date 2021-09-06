dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 첫번째 시도 - DFS + 백트래킹 -> 시간초과 80/100 점


def solution(board):
    global res

    def dfs(L, x, y, tot, dir):
        global res
        if tot + min((2*n-2-x-y)*100 + 500, (n-1-x)*100, (n-1-y)*100) > res:
            return
        if tot > res:
            return
        if x == n-1 and y == n-1:
            if res > tot:
                res = tot
            return
        else:
            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and board[nx][ny] == 0:
                    check[nx][ny] = 1
                    board[nx][ny] = 2
                    if L == 0:
                        dfs(L+1, nx, ny, tot, s)
                    elif L != 0 and s == dir:
                        dfs(L+1, nx, ny, tot+100, s)
                    elif L != 0 and s != dir:
                        dfs(L+1, nx, ny, tot+600, s)
                    check[nx][ny] = 0
                    board[nx][ny] = 0

    n = len(board)
    check = [[0]*n for _ in range(n)]
    check[0][0] = 1
    board[0][0] = 2
    res = 1e9
    dfs(0, 0, 0, 100, -1)

    return res

# 두번째 시도 - DFS + dp


dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def solution2(board):
    global res

    def dfs(L, x, y, tot, dir):
        global res

        # dp 리스트에 저장된 값보다 코스트가 크다면 재귀 트리 자르기
        if dp[x][y] < tot:
            return

        # dp 에 저장
        if tot <= dp[x][y]:
            dp[x][y] = tot

        if tot > res:
            return
        if x == n-1 and y == n-1:

            if res > tot:
                res = tot
            return
        else:
            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and board[nx][ny] == 0:
                    check[nx][ny] = 1
                    board[nx][ny] = 2
                    if L == 0:
                        dfs(L+1, nx, ny, tot, s)
                    elif L != 0 and s == dir:
                        dfs(L+1, nx, ny, tot+100, s)
                    elif L != 0 and s != dir:
                        dfs(L+1, nx, ny, tot+600, s)
                    check[nx][ny] = 0
                    board[nx][ny] = 0

    n = len(board)
    check = [[0]*n for _ in range(n)]
    check[0][0] = 1
    board[0][0] = 2
    res = 1e9
    # 경로 코스트 저장할 dp 2차원 리스트
    dp = [[1e9]*25 for _ in range(25)]
    dfs(0, 0, 0, 100, -1)

    return res
