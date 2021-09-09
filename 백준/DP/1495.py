# 실버1 - 기타리스트
# dp
# 특이한 동전유형

# 핵심 아이디어 : 모든 볼륨에 대하여 연주 가능 여부 계산
# dp[i][j+1] -> i번째 노래일 때 j 크기의 볼륨으로 연주 가능한지 여부

# 곡번호 볼륨 dp테이블
#     / 0 1 2 3 4 5 6 7 8 9 10
#     / 0 0 0 0 0 1 0 0 0 0 0
# 1 5 / 1 0 0 0 0 0 0 0 0 0 1
# 2 3 / 0 0 0 1 0 0 0 1 0 0 0
# 3 7 / 1 0 0 0 0 0 0 0 0 0 1


n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j-v[i-1] >= 0:
            dp[i][j-v[i-1]] = 1
        if j+v[i-1] <= m:
            dp[i][j+v[i-1]] = 1

res = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        res = i
        break

print(res)
