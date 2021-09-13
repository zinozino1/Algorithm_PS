# 골드5 - 벼락치기
# dp

# 냅색 bounded 문제

n, t = map(int, input().split())
orders = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0]*(t+1)

for order in orders:
    time, score = order
    for i in range(t, time-1, -1):
        dp[i] = max(dp[i-time]+score, dp[i])

print(max(dp))
