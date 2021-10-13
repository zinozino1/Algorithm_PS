# 실버2 - 배열돌리기3
# 구현

global grid
n, m, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))


def one(n, m):  # 상하반전
    cnt = n//2
    for i in range(cnt):
        grid[i], grid[n-i-1] = grid[n-i-1][:], grid[i][:]


def two(n, m):  # 좌우반전
    cnt = m//2
    for c in range(cnt):
        for i in range(n):
            grid[i][c], grid[i][m - c - 1] = grid[i][m - c - 1], grid[i][c]


def three(n, m):  # 오른쪽 90도 회전
    global grid
    tmp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tmp[i][j] = grid[n-j-1][i]
    grid = [layer[:] for layer in tmp]


def four(n, m):  # 왼쪽 90도 회전
    global grid
    tmp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tmp[i][j] = grid[j][m-i-1]
    grid = [layer[:] for layer in tmp]


def five(n, m):  # 1->2, 2->3, 3->4, 4->1
    first = [grid[i][j] for i in range(n//2) for j in range(m//2)]
    second = [grid[i][j] for i in range(n//2) for j in range(m//2, m)]
    third = [grid[i][j] for i in range(n//2, n) for j in range(m//2, m)]
    fourth = [grid[i][j] for i in range(n//2, n) for j in range(m//2)]
    # 1->2
    for i in range(n//2):
        for j in range(m//2, m):
            grid[i][j] = first.pop(0)
    # 2->3
    for i in range(n//2, n):
        for j in range(m//2, m):
            grid[i][j] = second.pop(0)
    # 3->4
    for i in range(n//2, n):
        for j in range(m//2):
            grid[i][j] = third.pop(0)
    # 4->1
    for i in range(n//2):
        for j in range(m//2):
            grid[i][j] = fourth.pop(0)


def six(n, m):  # 1->4, 4->3, 3->2, 2->1
    first = [grid[i][j] for i in range(n // 2) for j in range(m // 2)]
    second = [grid[i][j] for i in range(n // 2) for j in range(m // 2, m)]
    third = [grid[i][j] for i in range(n // 2, n) for j in range(m // 2, m)]
    fourth = [grid[i][j] for i in range(n // 2, n) for j in range(m // 2)]

    # 1->4
    for i in range(n // 2, n):
        for j in range(m // 2):
            grid[i][j] = first.pop(0)
    # 4->3
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            grid[i][j] = fourth.pop(0)
    # 3->2
    for i in range(n // 2):
        for j in range(m // 2, m):
            grid[i][j] = third.pop(0)
    # 2->1
    for i in range(n // 2):
        for j in range(m // 2):
            grid[i][j] = second.pop(0)


for o in order:
    n, m = len(grid), len(grid[0])
    if o == 1:
        one(n, m)
    elif o == 2:
        two(n, m)
    elif o == 3:
        three(n, m)
    elif o == 4:
        four(n, m)
    elif o == 5:
        five(n, m)
    else:
        six(n, m)

for g in grid:
    print(*g)
print()
