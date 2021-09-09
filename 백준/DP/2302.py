# 실버1 - 극장
# dp

# 신기한 dp 규칙
# 피보나치 형태
# 규칙이 보이지 않을 떈 귀납법으로 해결하자
# vip 자석 제외 각 영역은 곱사건이 이루어진다
# 1 2 3 v 5 6 v 7 8 9 라면
# dp[3] * dp[2] * dp[3] 이렇게 된다는 말

# 저게 왜 dp[n]이냐 ? -> 노가다로 규칙 찾는다. -> 피보나치 형태로 귀결됨 -> 좌석을 자우로만 바꿔 배치할 수 있는 경우의 수는 피보나치 수열이 된다.
# 참고로 int범위에서 나타낼 수 있는 피보나치 수열 최대 44항

n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)]

dp = [0] * (n+1)
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

num_len = 0
res = 1
for i in range(1, n+1):

    if i in fixed:
        res *= dp[num_len]
        num_len = 0
    else:
        num_len += 1
    if i == n:
        res *= dp[num_len]

print(res)
