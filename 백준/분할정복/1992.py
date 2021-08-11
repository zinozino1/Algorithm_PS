# 실버1 - 쿼드트리
# 분할정복

# 1074와 유사

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

res = ''


def recur(size, x, y):
    global res
    onecnt = 0
    zerocnt = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if grid[i][j] == "1":
                onecnt += 1
            if grid[i][j] == "0":
                zerocnt += 1
    if onecnt == size*size:
        res += "1"
        return
    elif zerocnt == size*size:
        res += "0"
        return
    else:
        res += "("
        recur(size//2, x, y)
        recur(size//2, x, y+size//2)
        recur(size//2, x+size//2, y)
        recur(size//2, x+size//2, y+size//2)
        res += ")"


recur(n, 0, 0)
print(res)
