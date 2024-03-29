# 골드5 - 줄세우기
# dp

# 전형적인 LIS 문제이다..

n = int(input())
target = [int(input()) for _ in range(n)]

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if target[j] < target[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(n-max(dp))
