# 골드5 - 움직이는미로탈출
# BFS

# 반례 못찾아서 질문 반례참조
# 큐에 있는 원소 모두 돈다음에 그리드 업데이트 시켜야함
# 제자리에 있을 경우는 중복 체크 제외
# 벽에 만나서 사라진 좌표는 체크배열 초기화

from collections import deque

grid = [list(input().strip()) for _ in range(8)]
dx = [0, 1, 0, -1, 0, -1, 1, -1, 1]
dy = [1, 0, -1, 0, 0, -1, 1, 1, -1]

# 블록 이동시키는 함수


def move():
    for i in range(8):
        tmp = deque()
        for j in range(8):
            tmp.append(grid[j][i])
        tmp.appendleft(".")
        for j in range(8):
            grid[j][i] = tmp[j]


def bfs():
    q = deque()
    q.append((7, 0))
    check = [[0]*8 for _ in range(8)]
    check[7][0] = 1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == 0 and y == 7:
                return 1
            if grid[x][y] == "#":
                check[x][y] = 0
                continue
            for s in range(9):
                nx = x+dx[s]
                ny = y+dy[s]
                if 0 <= nx <= 7 and 0 <= ny <= 7 and grid[nx][ny] == ".":
                    if x == nx and y == ny:
                        q.append((nx, ny))
                    else:
                        if check[nx][ny] == 0:
                            check[nx][ny] = 1
                            q.append((nx, ny))

        move()
    return 0


print(bfs())
