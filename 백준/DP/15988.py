# 실버2-1,2,3더하기
# dp
# 14:10 - 14:25

# TLE 받았던 내 코드
# 어차피 같은 dp 테이블을 이용하는데 멍청하게 이중 반복문 안에서 또 dp 선언하고 있었음
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1 or n == 2:
        print(n)
        continue
    elif n == 3:
        print(4)
        continue
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] += dp[i - 1] % 1000000009
        dp[i] += dp[i - 2] % 1000000009
        dp[i] += dp[i - 3] % 1000000009

    print(dp[-1] % 1000000009)

    # 개선된 코드
    # dp 테이블을 공유하므로 문제에서 제공하는 최대 값으로 배열 잡고
    # dp 배열 참조만 하면 된다
    dp = [0 for i in range(1000001)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 1000001):
        dp[i] = dp[i - 1] % 1000000009 + \
            dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

    t = int(input())
    for i in range(t):
        n = int(input())
        print(dp[n] % 1000000009)
