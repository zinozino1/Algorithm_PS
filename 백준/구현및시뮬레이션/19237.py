# 골드3 - 청소년상어
# 시뮬레이션

from collections import defaultdict
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
info = [[[] for _ in range(n)] for _ in range(n)]
shark = [[0, 0, 0, 0]]
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            info[i][j].append([grid[i][j], k])
            shark.append([grid[i][j], i, j])
sharkdir = list(map(int, input().split()))
sharkdir = list(map(lambda x: x-1,  sharkdir))
sharkdic = defaultdict(list)
shark.sort(key=lambda x: x[0])
for i, dir in enumerate(sharkdir):
    shark[i+1].append(dir)
for i in range(m):
    for j in range(4):
        tmp = list(map(int, input().split()))
        tmp = list(map(lambda x: x-1, tmp))
        sharkdic[i+1].append(tmp)


time = 0
while True:
    if time > 1000:
        time = -1
        break
    # if 1번 상어만 격자에 남으면 종료
    cnt = 0
    for i in range(1, m+1):
        if shark[i] == [-1, -1, -1, -1]:
            cnt += 1

    if cnt == m-1 and shark[1] != [-1, -1, -1, -1]:
        break

    # 0. shark 기준으로 실행
    willmove = [[]]  # 상어들이 이동할 위치
    will_delete = []
    for i in range(1, m+1):  # i -> shark 번호
        snum, sx, sy, sd = shark[i]
        if snum == -1:
            willmove.append([-1, -1, -1])
            continue  # 제거된 상어

        # 상어 주변 탐색
        candi = []
        my = []
        target = []
        for s in range(4):
            nx = sx+dx[s]
            ny = sy+dy[s]
            if not (0 <= nx <= n-1 and 0 <= ny <= n-1):
                continue
            if len(info[nx][ny]) == 0:
                candi.append([nx, ny, s])  # x,y,방향

        if not candi:  # 후보가 없을 경우
            inner_candi = []
            for s in range(4):
                nx = sx + dx[s]
                ny = sy + dy[s]
                if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1):
                    continue
                if info[nx][ny][0][0] == snum:
                    inner_candi.append([nx, ny, s])

            flag = False
            for pd in sharkdic[snum][sd]:  # 우선순위 적용
                for can in inner_candi:
                    cx, cy, cd = can
                    if pd == cd:
                        target = can[:]
                        will_delete.append([cx, cy])
                        flag = True
                        break
                if flag:
                    break

        else:
            flag = False
            for pd in sharkdic[snum][sd]:  # 우선순위 적용
                for can in candi:
                    cx, cy, cd = can
                    if pd == cd:
                        target = can[:]
                        flag = True
                        break
                if flag:
                    break

        willmove.append(target)

    for wd in will_delete:
        x, y = wd
        info[x][y] = []

    # 냄새 1씩 감소
    for i in range(n):
        for j in range(n):
            for p in range(len(info[i][j])):
                info[i][j][p][1] -= 1
                if info[i][j][p][1] == 0:
                    info[i][j].pop(p)

    # 상어 이동
    for i in range(1, m+1):
        x, y, d = willmove[i]
        if d == -1:
            continue
        info[x][y].append([i, k])
        shark[i] = [i]
        shark[i].extend(willmove[i])

    # 쫓아내기
    # shark -1로 업데이트
    for i in range(n):
        for j in range(n):
            if len(info[i][j]) >= 2:
                willremove = []  # 제거될 상어 번호만 저장
                info[i][j].sort()
                while len(info[i][j]) != 1:
                    curr = info[i][j].pop()
                    num, d = curr
                    willremove.append(num)
                for w in willremove:
                    shark[w] = [-1]*4
    time += 1

print(time)
