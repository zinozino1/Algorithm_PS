# 골드3 - 가장 긴 바이토닉 증가 수열
# dp


# 증가수열 + 역 증가수열 조합으로 풀 수 있었음
# 우연히 발견한 규칙

n = int(input())
seq = list(map(int, input().split()))

dp = [1]*n
dp2 = [1]*n

# 증가수열
for i in range(1, n):
    maxN = 0
    for j in range(i):
        if seq[j] < seq[i] and maxN < dp[j]:
            maxN = dp[j]
    dp[i] = maxN + 1

# 역 증가수열
for i in range(n-1, -1, -1):
    maxN = 0
    for j in range(n-1, i, -1):
        if seq[j] < seq[i] and maxN < dp2[j]:
            maxN = dp2[j]
    dp2[i] = maxN + 1

maxN = -1e9

for i in range(n):
    maxN = max(maxN, dp[i]+dp2[i])
print(maxN-1)
