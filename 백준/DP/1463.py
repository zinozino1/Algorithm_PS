# 실버3-1로 만들기
# dp


def sol():
    n = int(input())
    if n == 1:
        print(0)
        return
    elif n == 2:
        print(1)
        return

    dp = [0]*(n+1)
    dp[2], dp[3] = 1, 1

    for i in range(4, n+1):
        if i % 2 == 0 and i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
        elif i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1

    print(dp[-1])


sol()
