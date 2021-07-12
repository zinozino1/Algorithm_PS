# 실버3-1,2,3 더하기
# dp


n = int(input())

for _ in range(n):
    m = int(input())
    if m == 1 or m == 2:
        print(m)
        continue
    if m == 3:
        print(4)
        continue
    dp = [0]*(m+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, m+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[-1])
