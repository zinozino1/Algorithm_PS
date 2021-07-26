# 실버1 - 정수 삼각형
# dp

# 무난한 dp 문제

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    triangle[i] += [0]*(5-len(triangle[i]))
if n == 1:
    print(triangle[0][0])
else:
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    dp[1][0], dp[1][1] = triangle[0][0] + \
        triangle[1][0], triangle[0][0]+triangle[1][1]

    for i in range(2, n):
        for j in range(i+1):
            if 0 < j < i:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1]+triangle[i][j]

    print(max(dp[n-1]))
