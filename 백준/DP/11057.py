# 실버1 - 오르막수
# dp
# dp[i][j] => i자릿수 숫자에서 j로 숫자가 끝나는 경우의 수
# 점화식 : dp[i][j] = dp[i-1][0]+dp[i-1][1]+...+dp[i-1][j-1]+dp[i-1][j]

n = int(input())

dp = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n+1)]
dp[1] = [1]*10
mod = 10007
for i in range(2, n+1):
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]
        dp[i][j] %= mod

print(sum(dp[n]) % mod)
