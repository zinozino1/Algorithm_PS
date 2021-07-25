# 골드4 - 레이저 통신
# BFS


# DFS 풀이 -> TLE
# 최단 거리를 구해야하므로 DFS는 적절하지 않다.
from collections import deque

w, h = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

startx, starty = 0, 0
endx, endy = 0, 0
inner_flag = False
for i in range(h):
    for j in range(w):
        if grid[i][j] == "C" and not inner_flag:
            startx, starty = i, j
            inner_flag = True
        if grid[i][j] == "C" and inner_flag:
            endx, endy = i, j


check = [[0]*w for _ in range(h)]
check[startx][starty] = 1
min_diff = 1e9


def dfs(L, x, y, dir, dir_cnt):
    global min_diff

    if x == endx and y == endy:
        if dir_cnt < min_diff:
            min_diff = dir_cnt
        return

    else:
        for s in range(4):
            nx = x+dx[s]
            ny = y+dy[s]

            if 0 <= nx <= h-1 and 0 <= ny <= w-1 and check[nx][ny] == 0 and (grid[nx][ny] == "." or grid[nx][ny] == "C"):
                check[nx][ny] = 1
                if s != dir:
                    dfs(L+1, nx, ny, s, dir_cnt+1)
                else:
                    dfs(L+1, nx, ny, s, dir_cnt)
                check[nx][ny] = 0


dfs(0, startx, starty, -1, 0)

print(min_diff-1)

# BFS 풀이
# 중복방문이어도 방향 전환 카운트 수가 낮으면 갱신해야된다.

w, h = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

startx, starty = 0, 0
endx, endy = 0, 0
inner_flag = False
for i in range(h):
    for j in range(w):
        if grid[i][j] == "C" and not inner_flag:
            startx, starty = i, j
            inner_flag = True
        if grid[i][j] == "C" and inner_flag:
            endx, endy = i, j

min_diff = 1e9


def bfs():
    global min_diff
    q = deque()
    q.append([startx, starty, -1, 0])
    vis = [[-1]*w for _ in range(h)]
    vis[startx][starty] = 0

    while q:

        for _ in range(len(q)):
            # 좌표, 방향, 방향바뀐 횟수
            x, y, dir, dir_cnt = q.popleft()
            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]

                # 큐에서 꺼낸 좌표주위에 "C"가 있다면 방향 카운트 최소값 업데이트
                if 0 <= nx <= h-1 and 0 <= ny <= w-1 and grid[nx][ny] == "C" and vis[nx][ny] == -1:
                    tmp_cnt = dir_cnt
                    if dir != s:
                        tmp_cnt += 1
                    if tmp_cnt < min_diff:
                        min_diff = tmp_cnt

                # "."이면 큐에 넣기 + 방향이 다르면 방향 카운트 증가
                if 0 <= nx <= h-1 and 0 <= ny <= w-1 and grid[nx][ny] == ".":
                    if vis[nx][ny] == -1:
                        if dir != s:
                            q.append([nx, ny, s, dir_cnt+1])
                            vis[nx][ny] = dir_cnt + 1
                        else:
                            q.append([nx, ny, s, dir_cnt])
                            vis[nx][ny] = dir_cnt
                    # 이미 방문된 좌표라도, dir_cnt가 더 낮으면 갱신
                    elif vis[nx][ny] != 0 and dir_cnt < vis[nx][ny]:
                        if dir != s:
                            q.append([nx, ny, s, dir_cnt+1])
                            vis[nx][ny] = dir_cnt + 1
                        else:
                            q.append([nx, ny, s, dir_cnt])
                            vis[nx][ny] = dir_cnt


bfs()
print(min_diff-1)
