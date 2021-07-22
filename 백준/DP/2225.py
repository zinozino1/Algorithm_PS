# 골드5 - 합분해
# dp


# 점화식 만드는 것이 어려워서 다른 사람 풀이 참조함
# 주의점 1. dp 테이블의 인덱스는 끝자리나 첫자리에 i가 오는 경우가 아님
#          i가 n일 떄를 뜻하는 것
# 주의점 2. k는 i를 만들 때 필요한 숫자의 갯수.

# 이런 문제는 직접 dp 테이블을 그려가며 규칙을 찾아야 할듯..

n, k = map(int, input().split())
mod = 1000000000
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
        dp[i][j] %= mod
print(dp[k][n])
