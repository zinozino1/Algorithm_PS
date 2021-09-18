# 실버2 - 점프
# dp

# 전형적인 dp라는데 처음본다
# 기존 격자 dp는 행 첫줄, 열 첫줄 먼저 셋팅해놓고 for i for j 로 쭉 내려오는 유형인데
# 이거는 점프를 뛰어버린다.

# dp[i][j] 가 1인 곳만 로직 시작한다.
# dp[i][j] == 1이어야지 갈 수 있는 곳이기 때문


# 오른쪽 아래쪽으로만 갈 수 있기 때문에 dp로 풀 수 있다.
# 만약 4방향이면 dp가 불가하고 DFS + dp로 풀어야한다.


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            break
        ni = i+grid[i][j]
        nj = j+grid[i][j]

        if 0 <= ni <= n-1:
            dp[ni][j] += dp[i][j]
        if 0 <= nj <= n-1:
            dp[i][nj] += dp[i][j]

print(dp[n-1][n-1])
