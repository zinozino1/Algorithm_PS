# LG 전자 sample test 2번


def solution():
    n = int(input())
    mushrooms = list(map(int, input().split()))

    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = mushrooms[0]

    for i in range(1, n):
        if i % 2 == 0:
            dp[i][0] = max(dp[i-1])+mushrooms[i]
            dp[i][1] = max(dp[i-1])
        else:
            dp[i][0] = max(dp[i-1])-mushrooms[i]
            dp[i][1] = max(dp[i-1])

    return max(dp[n-1])


print(solution())
