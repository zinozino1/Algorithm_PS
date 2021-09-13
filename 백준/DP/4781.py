#  골드5 - 사탕가게
# dp

# 냅색 - unbounded
# 부동 소수점 조심

while True:
    n, m = input().split()
    n, m = int(n), int(float(m)*100)
    if n == 0 and m == 0:
        break
    dp = [0]*(m+1)
    info = []
    for _ in range(n):
        k, c = map(float, input().split())
        info.append((int(k), int(c*100+0.5)))
    for i in info:
        kal, cost = i
        for j in range(cost, m+1):
            dp[j] = max(dp[j-cost]+kal, dp[j])
    print(max(dp))
