# 단순 구현
# 격자 외곽으로 나가면 방향 바뀌는 테크닉 중요

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(rows, columns, queries):
    grid = []
    cnt = 1
    for i in range(1, rows + 1):
        tmp = []
        for j in range(1, columns + 1):
            tmp.append(cnt)
            cnt += 1
        grid.append(tmp)
    res = []
    for q in queries:
        d = 0
        min_num = 1e9
        start_x, start_y, end_x, end_y = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        curr_pos = [start_x, start_y]
        prev_pos = [start_x, start_y]
        init_val = grid[start_x][start_y]

        while True:
            if curr_pos[0] + dx[d] > end_x or curr_pos[1] + dy[d] > end_y or curr_pos[0] + dx[d] < start_x or curr_pos[1] + \
                    dy[d] < start_y:
                d += 1
            if d == 4:
                break
            if grid[curr_pos[0]][curr_pos[1]] < min_num:
                min_num = grid[curr_pos[0]][curr_pos[1]]

            curr_pos = [curr_pos[0] + dx[d], curr_pos[1] + dy[d]]
            grid[prev_pos[0]][prev_pos[1]] = grid[curr_pos[0]][curr_pos[1]]
            prev_pos = curr_pos
        grid[start_x][start_y+1] = init_val
        res.append(min_num)

    return res
