# 골드3 - 벽 부수고 이동하기2
# BFS + dp?

# 최대 k개의 벽을 부술 수 있으므로 0,1,2,3...k 개의 벽을 부쉈을 때의 최단거리
# 3차원 리스트 정의
# 노션 문제풀이 사진 참고

from collections import deque

n, m, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
vis = [[[1e9]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    q = deque()
    vis[0][0][0] = 1
    q.append([0, 0, 0])
    while q:

        for _ in range(len(q)):
            # x,y,벽 부순 갯수
            x, y, z = q.popleft()

            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]

                if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                  # 벽 o
                  # 방문한적이 없고 부순 벽의 개수가 k개 이하
                    if grid[nx][ny] == "1" and z+1 <= k and vis[nx][ny][z+1] == 1e9:
                        vis[nx][ny][z+1] = vis[x][y][z]+1
                        q.append([nx, ny, z+1])
                  # 벽 x
                  # 방문한적만 없으면 된다
                    elif grid[nx][ny] == "0" and vis[nx][ny][z] == 1e9:
                        vis[nx][ny][z] = vis[x][y][z]+1
                        q.append([nx, ny, z])


bfs()
if min(vis[n-1][m-1]) == 1e9:
    print(-1)
else:
    print(min(vis[n-1][m-1]))
