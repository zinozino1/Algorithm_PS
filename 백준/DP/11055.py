# 실버2 - 가장 큰 증가 부분 수열
# dp

# 갯수가 아닌 값 저장하는 유형


n = int(input())
seq = list(map(int, input().split()))

dp = [0]*n
dp[0] = seq[0]

for i in range(1, n):
    tmp = []
    for j in range(i):
        if seq[i] > seq[j]:
            tmp.append(dp[j])
    if tmp:
        dp[i] = max(tmp)+seq[i]
    else:
        dp[i] = seq[i]

print(max(dp))

# 다른 풀이
# tmp 추가 배열을 이용하지 않아도 된다 .

n = int(input())
array = list(map(int, input().split()))

d = [1]*n
d[0] = array[0]
for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j]+array[i])
        else:
            d[i] = max(d[i], array[i])

print(max(d))
