# 실버3-이친수
# dp
# 연속된 자리수 유형

n = int(input())

if n == 1:
    print(1)
else:

    dp = [[0]*2 for _ in range(n+1)]
    dp[1] = [0, 1]
    dp[2] = [1, 0]

    for i in range(3, n+1):
        dp[i][0] = dp[i-1][0]+dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    print(sum(dp[n]))
