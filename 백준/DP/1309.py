# 실버1 - 동물원
# dp

# dp[i][0] = 칸수가 2*i개 있을 때 사자가 위에 배치되는 경우의 수
# dp[i][1] = 칸수가 2*i개 있을 때 사자가 아래에 배치되는 경우의 수
# dp[i][2] = 칸수가 2*i개 있을 때 사자가 배치되지 않는 경우의 수

n = int(input())

dp = [[0]*3 for _ in range(n+1)]
dp[1] = [1, 1, 1]
mod = 9901

for i in range(2, n+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = dp[i-1][1]+dp[i-1][2]
            dp[i][j] %= mod
        elif j == 1:
            dp[i][j] = dp[i-1][0]+dp[i-1][2]
            dp[i][j] %= mod
        else:
            dp[i][j] = dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
            dp[i][j] %= mod

print(sum(dp[n]) % mod)
