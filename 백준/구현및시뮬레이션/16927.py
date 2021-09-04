# 실버1 - 배열돌리기 2
# 구현


n, m, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def lotate():
    depth = int(min(n, m) / 2 + 0.5)
    for d in range(depth):
        first = grid[d][d]
        # left
        for col in range(d+1, m-d):
            grid[d][col-1] = grid[d][col]
        # up
        for row in range(d+1, n-d):
            grid[row-1][m-d-1] = grid[row][m-d-1]
        # right
        for col in range(m-2-d, d-1, -1):
            grid[n-1-d][col+1] = grid[n-1-d][col]
        # down
        for row in range(n-2-d, d-1, -1):
            grid[row+1][d] = grid[row][d]

        grid[d+1][d] = first


for _ in range(r % (2*(n+m-2))):
    lotate()

for g in grid:
    print(*g)
