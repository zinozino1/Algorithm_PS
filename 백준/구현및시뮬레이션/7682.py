# 골드5 - 틱택토
# 구현


while True:
    target = input().strip()
    if target == "end":
        break

    grid = [list(target[:3]), list(target[3:6]), list(target[6:9])]

    o_cnt, x_cnt = 0, 0
    # for g in grid:
    #   print(g)
    for g in grid:
        o_cnt += g.count("O")
        x_cnt += g.count("X")

    x_flag = False
    o_flag = False
    for g in grid:
        if g.count("X") == 3:
            x_flag = True
        if g.count("O") == 3:
            o_flag = True
    for g in zip(*grid):
        if g.count("X") == 3:
            x_flag = True
        if g.count("O") == 3:
            o_flag = True

    local_x_cnt = 0
    local_o_cnt = 0
    for i in range(3):
        for j in range(3):
            if i == j and grid[i][j] == "X":
                local_x_cnt += 1
            if i == j and grid[i][j] == "O":
                local_o_cnt += 1
    if local_x_cnt == 3:
        x_flag = True
    if local_o_cnt == 3:
        o_flag = True

    local_x_cnt = 0
    local_o_cnt = 0
    for i in range(3):
        if grid[i][3-i-1] == "X":
            local_x_cnt += 1
        if grid[i][3-i-1] == "O":
            local_o_cnt += 1
    if local_x_cnt == 3:
        x_flag = True
    if local_o_cnt == 3:
        o_flag = True
    if x_flag and o_flag:
        print("invalid")
        continue

    elif x_flag and not o_flag:
        if o_cnt != x_cnt - 1:
            print("invalid")
            continue

    elif not x_flag and o_flag:
        if o_cnt != x_cnt:
            print("invalid")
            continue

    elif not x_flag and not o_flag:
        if o_cnt + x_cnt != 9:
            print("invalid")
            continue
        else:
            if o_cnt + 1 != x_cnt:
                print("invalid")
                continue

    print("valid")
