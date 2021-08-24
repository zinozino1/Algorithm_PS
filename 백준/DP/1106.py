# 실버2 - 호텔
# dp


# 동전 유형


c, n = map(int, input().split())
ad = []
for _ in range(n):
    cash, cumster_num = map(int, input().split())
    ad.append((cash, cumster_num))

dp = [1e9]*(c+1)
start = ad[0][1]
for i in range(start):
    if i > c:
        break
    dp[i] = ad[0][0]
dp[0] = 0

for a in ad:
    cash, cumster_num = a

    for i in range(cumster_num):
        if i > c:
            break
        dp[i] = min(dp[i], cash)
    for i in range(cumster_num, c+1):
        dp[i] = min(dp[i], dp[i-cumster_num]+cash)

print(dp[c])
