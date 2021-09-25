def solution(weights, head2head):

    n = len(weights)
    people = [[0]*4 for _ in range(n)]
    for i in range(n):
        win = 0
        heavy_cnt = 0
        game_cnt = 0
        for j in range(n):
            if head2head[i][j] == "N":
                continue
            else:
                if head2head[i][j] == "W":
                    win += 1
                    if weights[i] < weights[j]:
                        heavy_cnt += 1
                game_cnt += 1
        if game_cnt == 0:
            people[i][0] = 0
        else:
            people[i][0] = win/game_cnt
        people[i][1] = heavy_cnt
        people[i][2] = weights[i]
        people[i][3] = i

    people.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    return [p[3]+1 for p in people]
