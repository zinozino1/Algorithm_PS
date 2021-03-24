# 골드4-아기상어
# DFS vs BFS => 최단 경로: BFS, 경로의 수: DFS
# 사실 최단경로도 DFS로 풀 수 있긴하나 매우 비효율적임
# 이것은 근본이니 외우는 것이 좋겠다


import sys
from collections import deque
input = sys.stdin.readline


def sol():

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = int(input())

    space = [list(map(int, input().split())) for _ in range(n)]

    shark_x = 0
    shark_y = 0
    shark_weight = 2
    eating_cnt = 0
    tot_time = 0

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                shark_x = i
                shark_y = j

    # BFS 여러번 돌려야 하므로 무한 루프
    while True:
        q = deque()
        q.append((shark_x, shark_y))
        check = [[0] * n for _ in range(n)]
        check[shark_x][shark_y] = 1
        tmp = []
        dis = 0

        # BFS 루프 한 번 돌기
        while q:
            for i in range(len(q)):
                curr_pos = q.popleft()
                # 후보 추리는 작업 -> 물고기 크기가 무조건 상어크기보다 작아야함
                if space[curr_pos[0]][curr_pos[1]] != 0 and curr_pos != (shark_x, shark_y) and space[curr_pos[0]][curr_pos[1]] < shark_weight:
                    tmp.append((dis, curr_pos[0], curr_pos[1]))

                for s in range(4):
                    nx = curr_pos[0]+dx[s]
                    ny = curr_pos[1]+dy[s]
                    # 이동하는 작업 -> 물고기 크기가 상어크기보다 작거나 같아도 됨
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and space[nx][ny] <= shark_weight and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        q.append((nx, ny))
            dis += 1  # 레벨 하나 증가
        tmp.sort(key=lambda x: (x[0], x[1], x[2]))

        # 후보가 없으면 브레이크
        if not tmp:
            break
        space[shark_x][shark_y] = 0
        shark_x = tmp[0][1]
        shark_y = tmp[0][2]
        tot_time += tmp[0][0]
        space[shark_x][shark_y] = 9
        eating_cnt += 1

        if eating_cnt == shark_weight:
            shark_weight += 1
            eating_cnt = 0

    print(tot_time)


sol()
