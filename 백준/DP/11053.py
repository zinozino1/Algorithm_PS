# 실버2-최대부분증가수열
# n^2임
# i부터 인덱스 0 까지 역으로 다시 순회하며 dp 업데이트

n = int(input())
target = list(map(int, input().split()))
dp = [1] * n
dp[0] = 1

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if target[j] < target[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
