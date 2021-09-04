# 골드4 - 배열돌리기 4
# 구현


import itertools as it

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
order = [tuple(map(int, input().split())) for _ in range(k)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def lotate(x1, y1, x2, y2):

    local_copied = [layer[:] for layer in copied]
    tmp_min = min(abs(x1-x2), abs(y1-y2))
    start_pos = []
    for i in range(tmp_min // 2 + 1):
        start_pos.append((x1+i, y1+i))

    check = [[0]*m for _ in range(n)]

    for pos in start_pos:
        x, y = pos
        d = 0
        while True:
            nx = x+dx[d]
            ny = y+dy[d]
            if nx > x2 or nx < x1 or ny < y1 or ny > y2 or check[nx][ny] == 1:
                d = (d+1) % 4
                if d == 0:
                    break
                continue
            copied[nx][ny] = local_copied[x][y]
            x, y = nx, ny
            check[nx][ny] = 1


minVal = 1e9

for curr in it.permutations(order):
    copied = [layer[:] for layer in grid]
    for next_order in curr:
        x1, y1 = next_order[0]-next_order[2], next_order[1]-next_order[2]
        x2, y2 = next_order[0]+next_order[2], next_order[1]+next_order[2]

        lotate(x1-1, y1-1, x2-1, y2-1)

    local_min = 1e9
    for low in copied:
        local_min = min(local_min, sum(low))
    minVal = min(local_min, minVal)


print(minVal)
