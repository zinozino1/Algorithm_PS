# 완전 탐색
# 매우 쉬움

def solution(numbers, target):
    global cnt
    cnt = 0

    def dfs(L, tot):
        global cnt
        if L == len(numbers):
            if tot == target:
                cnt += 1
            return
        else:
            dfs(L+1, tot+numbers[L])
            dfs(L+1, tot-numbers[L])

    dfs(0, 0)

    return cnt
