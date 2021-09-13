# 실버1 - Coins
# dp

# 전형적인 동전 유형

T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    print(dp[m])
