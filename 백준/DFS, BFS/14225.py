# 실버1-부분수열의 합
# DFS

# 무난한 DFS문제. 엣지케이스 처리 중요

n = int(input())
seq = list(map(int, input().split()))

res = []


def dfs(L, tot):
    if L == n:
        if tot != 0:
            res.append(tot)
        return
    else:
        dfs(L+1, tot+seq[L])
        dfs(L+1, tot)


dfs(0, 0)
res = sorted(set(res))

if n == 1:
    if res[0] != 1:
        print(1)
    else:
        print(2)

elif res[0] != 1:
    print(1)
else:
    next = res[1]
    prev = res[0]
    idx = 2
    while next == prev+1 and idx <= len(res)-1:
        prev = next
        next = res[idx]
        idx += 1
    if next == res[len(res)-1]:
        print(next+1)
    else:
        print(prev+1)
