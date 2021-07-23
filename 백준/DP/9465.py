# 실버2 - 스티커
# DP

# dp[i][j]
# j == 0 칸수가 i이고 해당칸이 i일때 스티커를 뗴지 않았을 때 점수 최대값
# j == 1 칸수가 i이고 해당칸이 i일때 해당 칸의 위쪽 스티커를 뗐을 때 최대값
# j == 2 칸수가 i이고 해당칸이 i일때 해당 칸의 아래쪽 스티커를 뗐을 때 최대값

# 범위 주의... 꼭 n==1일때 넣어보자

T = int(input())

for _ in range(T):
    n = int(input())
    tmp = [list(map(int, input().split())) for _ in range(2)]
    stickers = []
    for i in range(n):
        stickers.append((tmp[0][i], tmp[1][i]))

    dp = [[0]*3 for _ in range(n)]
    dp[0] = [0, stickers[0][0], stickers[0][1]]

    for i in range(n):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i-1])
            elif j == 1:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2])+stickers[i][0]
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1])+stickers[i][1]
    print(max(dp[n-1]))
