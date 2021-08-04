# 골드5 - 평범한 배낭
# dp 냅색

# 1개만 들어갈 수 있으므로 뒤에서 접근해야함 -> 중복 x

n, k = map(int, input().split())
dp = [0]*(k+1)

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i-w]+v, dp[i])

print(dp[k])
