# 골드4 - RGB 거리2
# dp

# 규칙 찾느라 한참 고생함

n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]

dp = [[[int(1e9)] * 3 for _ in range(3)] for _ in range(n - 1)]
dp.append([0, 0, 0])
dp[0][0][0] = RGB[0][0]
dp[0][1][1] = RGB[0][1]
dp[0][2][2] = RGB[0][2]

for i in range(1, n):
    if i != n - 1:
        dp[i][0][0] = min(dp[i - 1][1][0], dp[i - 1][2][0]) + RGB[i][0]
        dp[i][0][1] = min(dp[i - 1][1][1], dp[i - 1][2][1]) + RGB[i][0]
        dp[i][0][2] = min(dp[i - 1][1][2], dp[i - 1][2][2]) + RGB[i][0]

        dp[i][1][0] = min(dp[i - 1][0][0], dp[i - 1][2][0]) + RGB[i][1]
        dp[i][1][1] = min(dp[i - 1][0][1], dp[i - 1][2][1]) + RGB[i][1]
        dp[i][1][2] = min(dp[i - 1][0][2], dp[i - 1][2][2]) + RGB[i][1]

        dp[i][2][0] = min(dp[i - 1][0][0], dp[i - 1][1][0]) + RGB[i][2]
        dp[i][2][1] = min(dp[i - 1][0][1], dp[i - 1][1][1]) + RGB[i][2]
        dp[i][2][2] = min(dp[i - 1][0][2], dp[i - 1][1][2]) + RGB[i][2]
    else:
        dp[i][0] = min(dp[i - 1][1][1], dp[i - 1][1][2],
                       dp[i - 1][2][1], dp[i - 1][2][2]) + RGB[i][0]
        dp[i][1] = min(dp[i - 1][0][0], dp[i - 1][0][2],
                       dp[i - 1][2][0], dp[i - 1][2][2]) + RGB[i][1]
        dp[i][2] = min(dp[i - 1][0][0], dp[i - 1][0][1],
                       dp[i - 1][1][0], dp[i - 1][1][1]) + RGB[i][2]

print(min(dp[n-1]))
