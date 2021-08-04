# 실버1 - 이동하기
# dp

# n == 1000이라 dfs, bfs 불가능

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = grid[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1] + grid[i][j]
        if i > 0 and j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])+grid[i][j]

print(dp[n-1][m-1])
