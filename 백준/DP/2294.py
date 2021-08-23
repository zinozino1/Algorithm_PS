# 실버1 - 동전2
# dp

# 그리디 동전 문제와 유사하다. -> 하지만 그리디로 풀 수 있다는 정당성이 없으므로 dp 활용해야 한다.
# dp 동전1 문제와 유사하다. -> 하지만 이것은 모든 경우의 수가 아니라 최소값임

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1e9]*(k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i-coin]+1, dp[i])

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])
