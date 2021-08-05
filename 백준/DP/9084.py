# 골드5 - 동전
# dp

# 냅색 응용

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [[0]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(0, target+1):
            tmp = 0
            for k in range(j, -1, -coins[i-1]):
                tmp += dp[i-1][k]
            dp[i][j] = tmp

    print(dp[n][target])

# 개선된 풀이 -> 누적합이라는 것이 중요
T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(coins[i-1], m+1):
            dp[j] += dp[j-coins[i-1]]

    print(dp[m])
