# 실버2 - 가장 긴 감소하는 수열
# dp


# tmp안쓰고 푸는 방법을 익힐것

n = int(input())
seq = list(map(int, input().split()))

dp = [1]*n
res = 0
for i in range(1, n):
    maxN = 0
    for j in range(i):
        # max 값 갱신 tmp(max)의 로직과 같다.
        if seq[j] > seq[i] and dp[j] > maxN:
            maxN = dp[j]
    dp[i] = maxN + 1

print(max(dp))
