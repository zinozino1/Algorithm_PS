# 실버1 - 별찍기10
# 분할정복


# 0,0부터 시작
# 사이즈가 3이 나올때까지 분해한다.
# 분할된 영역의 첫 좌표를 찾는다.


n = int(input())

res = [[" "]*n for _ in range(n)]


def recur(size, x, y):
    if size == 3:
        res[x][y] = "*"
        res[x][y + 1] = "*"
        res[x][y + 2] = "*"
        res[x + 1][y] = "*"
        res[x + 1][y + 2] = "*"
        res[x + 2][y] = "*"
        res[x + 2][y + 1] = "*"
        res[x + 2][y + 2] = "*"

    else:
        recur(size // 3, x, y)
        recur(size // 3, x, y+size//3)
        recur(size // 3, x, y+size//3*2)
        recur(size // 3, x+size//3, y)
        recur(size // 3, x+size//3, y+size//3*2)
        recur(size // 3, x+size//3*2, y)
        recur(size // 3, x+size//3*2, y+size//3)
        recur(size // 3, x+size//3*2, y+size//3*2)


recur(n, 0, 0)
for r in res:
    print("".join(r))
