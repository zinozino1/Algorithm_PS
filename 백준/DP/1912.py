# 실버2-연속합
# dp


n = int(input())
seq = list(map(int, input().split()))

dp = [0]*n
dp[0] = seq[0]

for i in range(1, n):
    dp[i] = max(seq[i], dp[i-1]+seq[i])

print(max(dp))
