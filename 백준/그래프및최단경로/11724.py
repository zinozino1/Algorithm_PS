# 실버2 - 연결요소의 개수
# 그래프 + dfs

# 연결되어있는지 확인하면 된다 .

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)


def dfs(v):
    for next in node[v]:
        if check[next] == 0:
            check[next] = 1
            dfs(next)


check = [0]*(n+1)
cnt = 0

for i in range(1, n+1):
    if check[i] == 0:
        check[i] = 1
        dfs(i)
        cnt += 1

print(cnt)
