# 실버1 - 동전1
# dp

# 메모리 제한이 있기 때문에 1차원리스트로 풀어야함
# 시간제한도 짧기 때문에 이중 포문을 최대한 쓰지 않고 일차원 리스트에 덮어쓰는 식으로 풀이해야함
# 누적합이 핵심이다.

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]
print(dp[k])

# 1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 2: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
# 5: [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
