# 실버1-카드 구매하기 2
# dp
# 카드 구매하기 1의 최솟값 버전

# 그림 그려가며 해야함 헷갈림


n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)

dp = [0]*(n+1)
dp[1] = p[1]
dp[2] = min(p[1]*2, p[2])

for i in range(3, n+1):
    tmp_min = 1e9
    for j in range(1, i):
        if dp[j]+p[i-j] < tmp_min:
            tmp_min = dp[j]+p[i-j]
    dp[i] = min(tmp_min, p[i])


print(dp[-1])
