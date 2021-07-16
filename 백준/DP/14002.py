# 골드4-가장 긴 증가하는 부분수열 4
# dp
# 풀긴 풀었는데 약간 어거지로 풀었음
# dp는 갯수, res는 값들의 집합을 뜻함
# dp와 res는 같은 로직

# 가장 긴 증가하는 수열의 길이를 구하고 해당 길이의 위치를 구한다
# 위치를 통해 인덱스를 찾고 dp 배열을 검사한다.

n = int(input())
target = list(map(int, input().split()))

dp = [1] * n
res = [[] for _ in range(n)]

for i, t in enumerate(target):
    res[i].append(t)

for i in range(n):
    tmp = []
    tmp_arr = []
    for j in range(i - 1, -1, -1):
        if target[i] > target[j]:
            tmp.append(dp[j])
            tmp_arr.append((target[j], j, res[j]))

    if tmp:
        dp[i] = max(dp[i], max(tmp) + 1)
        res[i] += max(tmp_arr, key=lambda x: (len(x[2])))[2]

print(max(dp))
print(*max(res, key=len)[::-1])
