# 실버1 - Z
# 분할 정복


import sys
n, r, c = map(int, input().split())
cnt = 0


def recur(L, x, y):
    global cnt
    if x == r and y == c:
        print(cnt)
        sys.exit(0)
    if L == 1:
        cnt += 1
        return
    if not (x <= r < x + L and y <= c < y + L):
        cnt += L * L
        return

    recur(L//2, x, y)
    recur(L//2, x, y+L//2)
    recur(L//2, x+L//2, y)
    recur(L//2, x+L//2, y+L//2)


recur(2**n, 0, 0)
