# 실버2 - 행렬
# 그리디


# 최적의 선택은 "반드시 뒤집어야 하는 칸을 뒤집되, 뒤집는 횟수를 최소화하는 것"
# 어렵다..

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
target = [list(input().strip()) for _ in range(n)]


def check():
    for s in range(n):
        for a in range(m):
            if grid[s][a] != target[s][a]:
                return False
    return True


def flip(x, y):
    for k in range(x, x+3):
        for l in range(y, y+3):
            if grid[k][l] == "0":
                grid[k][l] = "1"
            else:
                grid[k][l] = "0"


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if grid[i][j] != target[i][j]:
            flip(i, j)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)
