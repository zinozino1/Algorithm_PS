# 실버3 - 계단오르기
# dp

# dp[0][i] => i-1번째 계단으로부터 온 점수 최대값
# dp[1][i] => i-2번째 계단으로부터 온 점수 최대값

n = int(input())
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
else:
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[0][1] = arr[0], arr[0]+arr[1]
    dp[1][0], dp[1][1] = 0, arr[1]

    for i in range(2, n):
        dp[0][i] = dp[1][i-1]+arr[i]
        dp[1][i] = max(dp[1][i-2], dp[0][i-2])+arr[i]

    print(max(dp[0][n-1], dp[1][n-1]))
