# 실버1 - 에너지 모으기
# 기본 DFS

# DFS 인자 -> 재귀 트리 가지마다 다른 값
# DFS 외부 -> 재귀 트리가 공유하는 변수나 값

n = int(input())
target = list(map(int, input().split()))
max_n = -1e9


def dfs(L, tot):
    global max_n
    if L == n-2:
        if tot > max_n:
            max_n = tot
        return
    else:
        for i in range(1, len(target)-1):
            curr, prev, next = target[i], target[i-1], target[i+1]
            del target[i]
            dfs(L+1, tot+prev*next)
            target.insert(i, curr)


dfs(0, 0)
print(max_n)
