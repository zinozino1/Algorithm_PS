# 실버1-RGB거리
# dp

# 완탐인가? -> 3^1000이라 불가
# 그리디인가 ? -> 반례 존재
# 그렇다면 dp지

n = int(input())
RGBS = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = RGBS[0][0]
dp[0][1] = RGBS[0][1]
dp[0][2] = RGBS[0][2]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1] + RGBS[i][0], dp[i-1][2] + RGBS[i][0])
        elif j == 1:
            dp[i][j] = min(dp[i-1][0] + RGBS[i][1], dp[i-1][2] + RGBS[i][1])
        elif j == 2:
            dp[i][j] = min(dp[i-1][0] + RGBS[i][2], dp[i-1][1] + RGBS[i][2])

print(min(dp[n-1]))
