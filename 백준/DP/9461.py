# 실버3 - 파도반 수열
# dp

T = int(input())
dp = [0]*101
tmp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i, t in enumerate(tmp):
    dp[i] = t

cnt = 3
for i in range(10, 101):
    dp[i] = dp[i-1]+dp[i-5]
    cnt += 1

for _ in range(T):
    n = int(input())
    print(dp[n-1])
