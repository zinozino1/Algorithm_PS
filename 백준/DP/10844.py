# 실버1 - 쉬운 계단수
# dp
# 숫자 자리수 때문에 2차원 dp 사용
# dp[i][j] => i자릿수 숫자에서 j가 숫자 맨 앞에 오는 경우

n = int(input())

if n == 1:
    print(9)
else:
    mod = 1000000000
    dp = [[0] * 10 for _ in range(n + 1)]

    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dp[2] = [0, 2, 2, 2, 2, 2, 2, 2, 2, 1]

    for i in range(3, n + 1):
        for j in range(1, 10):
            if j == 1:
                dp[i][j] = (dp[i - 2][j] + dp[i - 1][j + 1]) % mod
            elif j == 9:
                dp[i][j] = (dp[i - 1][j - 1]) % mod
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
    print(sum(dp[n]) % mod)
