# 골드5 - 가장 큰 정사각형
# dp

# dp문제임을 캐치하는 것이 중요
# 어디 하나라도 짧으면 그 길이가 최대길이로 저장됨 (정사각형을 만들수있는 최대길이)

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0] = grid[0][:]
for i in range(m):
    if i == 0:
        for j in range(n):
            dp[j][i] = grid[j][i]

maxN = -1e9
for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] == 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            maxN = max(maxN, dp[i][j])

for i in range(n):
    for j in range(m):
        if dp[i][j] > maxN:
            maxN = dp[i][j]
print(maxN**2)
