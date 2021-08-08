# 골드2 - 새로운 게임2
# 시뮬레이션

# 변수 설정이 중요 ..

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
horse_info = []
horse_map = [[[] for _ in range(n)] for _ in range(n)]
for num in range(k):
    x, y, d = map(int, input().split())
    horse_info.append([x-1, y-1, d])
    horse_map[x-1][y-1].append(num)

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

level = 0
flag = False
while True:

    if flag:
        break
    if level >= 1000:
        break

    for i in range(len(horse_info)):
        x, y, d = horse_info[i]

        nx = x+dx[d]
        ny = y+dy[d]

        curr_horse1 = horse_map[x][y][:]  # 현재 말이 있는 위치에 있는 모든 말들
        curr_horse2 = horse_map[x][y][:]

        white_horse = []  # 가야할 칸이 하얀색이라면 갈 말들
        while curr_horse1 and curr_horse1[-1] != i:
            white_horse.append(curr_horse1.pop())
        if curr_horse1:
            white_horse.append(curr_horse1.pop())

        red_horse = []  # 가야할 칸이 빨간색이라면 갈 말들
        tmp = []
        while curr_horse2 and curr_horse2[-1] != i:
            tmp.append(curr_horse2.pop())
        if curr_horse2:
            tmp.append(curr_horse2.pop())

        while tmp[::-1]:
            red_horse.append(tmp.pop())

        # 파란색 or 좌표 벗어남
        if not (0 <= nx <= n-1 and 0 <= ny <= n-1) or grid[nx][ny] == 2:
            nd = -1
            if d == 1:
                nd = 2
            elif d == 2:
                nd = 1
            elif d == 3:
                nd = 4
            elif d == 4:
                nd = 3

            nnx = x+dx[nd]  # 새 좌표
            nny = y+dy[nd]

            horse_info[i][2] = nd  # 방향 먼저 바꿔줌

            # 파란색 -> 파란색 or 좌표 벗어남
            if not (0 <= nnx <= n-1 and 0 <= nny <= n-1) or grid[nnx][nny] == 2:
                # 아무 일도 일어나지 않음
                pass

            # 파란색 -> 하얀색
            elif grid[nnx][nny] == 0:
                # 원래 자리에 curr_horse1 넣어줌
                # 새로운 자리에 white_horse 넣어줌
                # white_horse 통해서 horse_info 업데이트 시켜줌
                horse_map[x][y] = curr_horse1[:]
                for k in range(len(white_horse)):
                    horse_info[white_horse[k]][0] = nnx
                    horse_info[white_horse[k]][1] = nny
                while white_horse:
                    horse_map[nnx][nny].append(white_horse.pop())

            # 파란색 -> 빨간색
            elif grid[nnx][nny] == 1:
                # 원래 자리에 curr_horse2 넣어줌
                # 새로운 자리에 red_horse 넣어줌
                # red_horse 통해서 horse_info 업데이트
                horse_map[x][y] = curr_horse2[:]
                for k in range(len(red_horse)):
                    horse_info[red_horse[k]][0] = nnx
                    horse_info[red_horse[k]][1] = nny
                while red_horse:
                    horse_map[nnx][nny].append(red_horse.pop())

        # 하얀색
        elif grid[nx][ny] == 0:
            horse_map[x][y] = curr_horse1[:]
            for k in range(len(white_horse)):
                horse_info[white_horse[k]][0] = nx
                horse_info[white_horse[k]][1] = ny
            while white_horse:
                horse_map[nx][ny].append(white_horse.pop())

        # 빨간색
        elif grid[nx][ny] == 1:
            horse_map[x][y] = curr_horse2[:]
            for k in range(len(red_horse)):
                horse_info[red_horse[k]][0] = nx
                horse_info[red_horse[k]][1] = ny
            while red_horse:
                horse_map[nx][ny].append(red_horse.pop())

        for p in range(n):
            for q in range(n):
                if len(horse_map[p][q]) >= 4:
                    flag = True
    level += 1

if level == 1000:
    print(-1)
else:
    print(level)
