# 실버1 - 포도주 시식
# dp
# 규칙 찾기 매우 어려움

n = int(input())
target = [int(input()) for _ in range(n)]
target.insert(0, 0)
dp = [0]*(n+1)
if n == 1:
    print(target[1])
else:
    dp[1] = target[1]
    dp[2] = target[1]+target[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+target[i], dp[i-3]+target[i-1]+target[i])

    print(dp[n])
