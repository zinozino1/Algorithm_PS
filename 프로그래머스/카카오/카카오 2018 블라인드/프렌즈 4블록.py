def gravity(m, n, board):
    for i in range(n):
        tmp = []
        for j in range(m):
            if board[j][i] != " ":
                tmp.append(board[j][i])
                board[j][i] = " "

        for j in range(m-1, -1, -1):
            if tmp:
                board[j][i] = tmp.pop()
    return [row[:] for row in board]


def solution(m, n, board):

    ans = 0
    list_board = [list(b) for b in board]
    while True:

        fin_flag = True
        candi = set()
        for i in range(m-1):
            for j in range(n-1):
                target = list_board[i][j]
                if target != " " and list_board[i][j+1] == target and list_board[i+1][j] == target and list_board[i+1][j+1] == target:
                    fin_flag = False
                    candi.add((i, j))
                    candi.add((i, j+1))
                    candi.add((i+1, j))
                    candi.add((i+1, j+1))
        if fin_flag:
            break

        ans += len(candi)
        for c in candi:
            x, y = c
            list_board[x][y] = " "

        list_board = gravity(m, n, list_board)

    return ans
