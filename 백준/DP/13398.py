# 골드5 - 연속합 2
# dp

# dp[i][0] -> i번째 원소를 제거하지 않았을 때 최대값 (i번째 원소를 무조건 포함해야함)
# dp[i][1] -> i번째 원소를 제거했을 때 최대 값 . 만약 i번쨰 원소를 제거하려 했을 때
# 이전에 이미 제거 했다면 업데이트 시킨다

# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# -35에서 dp값 생각해보기

n = int(input())
target = list(map(int, input().split()))
if n == 1:
    print(target[0])
else:
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = target[0]
    dp[0][1] = 0
    max_n = -1e9
    for i in range(1, n):
        dp[i][0] = max(target[i], dp[i-1][0]+target[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]+target[i])
        max_n = max(max_n, dp[i][1], dp[i][0])
    print(max_n)
