# 트리 + DFS

def solution(n, wires):
    global cnt

    def dfs(v, flag):
        global cnt
        for nxt in tree[v]:
            if check[nxt] == 0:
                if flag:
                    cnt += 1
                else:
                    cnt -= 1
                check[nxt] = 1
                dfs(nxt, flag)

    tree = [[] for _ in range(n+1)]
    for w in wires:
        s, e = w
        tree[s].append(e)
        tree[e].append(s)

    res = 1e9
    for w in wires:
        s, e = w
        tree[s].remove(e)
        tree[e].remove(s)

        check = [0] * (n+1)
        cnt = 0
        for i in range(1, n+1):
            if check[i] == 0 and cnt == 0:
                check[i] = 1
                dfs(i, True)
                cnt += 1

            elif check[i] == 0 and cnt != 0:
                check[i] = 1
                dfs(i, False)
                cnt -= 1

        if abs(cnt) < res:
            res = abs(cnt)

        tree[s].append(e)
        tree[e].append(s)

    return res
