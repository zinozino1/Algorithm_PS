# 골드5 - ABCDE
# 그래프

# 그래프의 깊이가 5이상인 노드를 찾으면 된다
# 백트래킹할 때 체킹을 풀어줘야함
# DFS 인자로 들어간 값은 따로 백트래킹 하지 않아도 리턴시 사라지게된다
# DFS 인자로 들어간 값은 재귀 트리마다 독립된 값을 가지고있음

n, m = map(int, input().split())
node = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)


def dfs(v, count):
    global flag
    if count >= 4:
        flag = True
    else:
        for k in node[v]:
            if check[k] == 0:
                check[k] = 1
                dfs(k, count+1)
                check[k] = 0


for i in range(n):
    check = [0]*n
    check[i] = 1
    flag = False
    dfs(i, 0)
    if flag:
        print(1)
        break
else:
    print(0)
