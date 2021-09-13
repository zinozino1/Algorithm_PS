# 실버1 - 민균이의 계략
# dp

# 전형적인 LIS 문제

n = int(input())
cards = list(map(int, input().split()))

dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if cards[j] < cards[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
