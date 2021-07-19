# 실버3 - 제곱수의 합
# dp 생각해내기가 매우 어려웠음


n = int(input())
dp = [x for x in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
print(dp[n])
