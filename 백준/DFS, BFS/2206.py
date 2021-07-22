# 골드4 - 벽 부수고 이동하기
# BFS + dp?


# 너무 어렵다
# 처음엔 벽좌표 하나하나 다 저장해서 그 좌표를 제거한 그리드 마다 BFS 돌리니까 TLE
# 이 방법은 BFS 한 번만 돌리면 된다.
# 최단거리, 방문여부를 동시에 만족하는 3차원 리스트 dis를 만들고
# 0번째에는 벽을 부수지 않을경우 최단거리, 1번째 인덱스에는 벽을 부술 경우 최단거리를 저장한다.

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dis = [[[-1, -1] for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    dis[0][0][0] = 1

    while q:
        for _ in range(len(q)):
            # x좌표, y좌표, 벽을 부쉈는가
            x, y, s = q.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                    # 벽이 아닌 경우 + 이 칸이 방문되지 않은 경우
                    # 벽이 아니면 s == 0, s == 1(전 경로애서 벽을 부쉈든 안 부쉈든 상관 없음 ) 둘 다 올 수 있음
                    if grid[nx][ny] == 0 and dis[nx][ny][s] == -1:
                        dis[nx][ny][s] = dis[x][y][s] + 1
                        q.append([nx, ny, s])
                    # 벽이고, 그 벽이 방문되지 않았고, 이전 블럭이 벽을 부수지 않았을 경우
                    # s == 0 만 올 수 있음 벽을 하나만 부술 수 있기 때문
                    elif grid[nx][ny] == 1 and dis[nx][ny][1] == -1 and s == 0:
                        dis[nx][ny][1] = dis[x][y][s] + 1
                        q.append([nx, ny, 1])


bfs()
if dis[n-1][m-1][0] == -1:
    print(dis[n-1][m-1][1])
elif dis[n-1][m-1][1] == -1:
    print(dis[n-1][m-1][0])
else:
    print(min(dis[n-1][m-1][1], dis[n-1][m-1][0]))
