# 실버2 - 연산자 끼워넣기 2
# DFS카운팅 테크닉

import sys

n = int(input())
target = list(map(int, input().split()))

plus, sub, mult, div = map(int, input().split())
max_n, min_n = -sys.maxsize, sys.maxsize


def dfs(L, tot):
    global plus, sub, mult, div, max_n, min_n
    if L == n-1:
        if tot > max_n:
            max_n = tot
        if tot < min_n:
            min_n = tot
        return
    else:

        if plus > 0:
            plus -= 1
            dfs(L+1, tot+target[L+1])
            plus += 1

        if sub > 0:
            sub -= 1
            dfs(L+1, tot-target[L+1])
            sub += 1

        if mult > 0:
            mult -= 1
            dfs(L+1, tot*target[L+1])
            mult += 1

        if div > 0:
            div -= 1
            dfs(L+1, int(tot/target[L+1]))
            div += 1


dfs(0, target[0])
print(max_n)
print(min_n)
