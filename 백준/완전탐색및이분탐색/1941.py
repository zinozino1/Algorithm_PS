import itertools as it
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def sol():

    # 연결 정보 : BFS를 통해 확인
    def bfs(arr):
        arr.sort(key=lambda x: (x[0], x[1]))
        start_x, start_y = arr[0]
        visited = [[0]*5 for _ in range(5)]
        visited[start_x][start_y] = 1
        q = deque()
        q.append((start_x, start_y))

        cnt = 0
        while q:
            cnt += len(q)
            for _ in range(len(q)):
                curr = q.popleft()
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= 4 and 0 <= ny <= 4 and (nx, ny) in arr and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

        if cnt == 7:
            return True
        else:
            return False

    # 이다솜이 4명 이상 있는가
    def is_leedasom(arr):
        cnt = 0
        for a in arr:
            x, y = a

            if grid[x][y] == "S":
                cnt += 1
        if cnt > 3:
            return True
        else:
            return False

    grid = [list(input().strip()) for _ in range(5)]
    check = []
    for i in range(5):
        for j in range(5):
            check.append((i, j))

    princess_cnt = 0
    # 격자에서 7개의 좌표 뽑는 경우의 수
    for tmp in it.combinations(check, 7):
      # 이다솜이 4명 이상인 좌표들만
        if is_leedasom(tmp):
          # 그 좌표들이 상하좌우로 인접해있는지 확인
            if bfs(list(tmp)):
                princess_cnt += 1

    print(princess_cnt)


sol()
