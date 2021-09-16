# 실버1 - 주지수
# dp

# 카카오에 그대로 나옴
# 각 격자마다 누적합을 계산해주면 된다. 일차원리스트와 크게 다를바 없음

# 무조건 dp[i][j]는 0,0부터 i,j까지의 합이어야한다.
# 0 row , col도 계산하기 위해 n+1,m+1 격자로 맞춰준다.

# 1. 합 점화식 -> dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
# 2. 범위에 맞는 값 구하기 -> dp[ex][ey] - dp[ex][sy-1] - dp[sx-1][ey] + dp[sx-1][sy-1]


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
num = int(input())
dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = grid[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + grid[i-1][j-1] - dp[i-1][j-1]

for _ in range(num):
    sx, sy, ex, ey = map(int, input().split())
    print(dp[ex][ey]-dp[ex][sy-1]-dp[sx-1][ey]+dp[sx-1][sy-1])
