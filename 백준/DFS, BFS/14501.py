# 실버4 - 퇴사
# DFS 풀이

# 건너뛰는 테크닉이라고 제발

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
max_n = -1e9


def dfs(L, tot):
    global max_n
    if L == n:
        max_n = max(max_n, tot)
        return
    else:
        if L+schedule[L][0] <= n:
            dfs(L+schedule[L][0], tot+schedule[L][1])
        dfs(L+1, tot)


dfs(0, 0)
print(max_n)


# dp 활용 풀이

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
schedule.insert(0, (0, 0))

dp = [0]*(n+1)


for i in range(1, n+1):
    if i+schedule[i][0] > n+1:
        dp[i] = max(dp)
        continue
    tmp = []
    for j in range(1, i):
        if j+schedule[j][0] <= i:
            tmp.append(dp[j])
    if tmp:
        dp[i] = max(tmp)+schedule[i][1]
    else:
        dp[i] = schedule[i][1]

print(max(dp))
