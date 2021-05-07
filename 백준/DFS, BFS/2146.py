# 골드3-다리만들기-BFS
# 처음에 섬들을 라벨링하고 라벨링 한 섬들 중 2개를 뽑는 DFS를 돌리려했으나 n<=100이므로 섬이 많아질 때 재귀가 깊어져
# TLE가 났음. 게다가 이 문제는 모든 섬들 사이의 거리 중 가장 최단거리를 구하는 문제임
# 따라서 각 섬의 엣지들 좌표를 저장한 후 abs 거리 공식을 통해 단순 반복문으로 최단거리를 구함
# 섬을 뚫는 다리가 있을 수 있어서 안된다 생각했는데 어차피 최단거리 다리므로 상관이 없음


import copy
import sys
from collections import deque
import itertools as it


def sol():
    global minN

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 섬 라벨링
    def labeling(x, y):
        check[x][y] = 1
        q = deque()
        q.append((x, y))
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                grid[curr[0]][curr[1]] = island_num

                # 각 섬의 엣지들 저장
                zero_cnt = 0
                for s in range(4):
                    nx = curr[0] + dx[s]
                    ny = curr[1] + dy[s]
                    if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and grid[nx][ny] == 0:
                        zero_cnt += 1
                if zero_cnt != 0:
                    tmp.append((curr[0], curr[1]))

                # 라벨링
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and grid[nx][ny] == 1:
                        check[nx][ny] = 1
                        q.append((nx, ny))

    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    check = [[0]*n for _ in range(n)]
    island_num = -1
    minN = 1e9
    edges = []

    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and grid[i][j] == 1:
                tmp = []
                grid[i][j] = island_num
                labeling(i, j)
                island_num -= 1
                edges.append(tmp)

    # 섬들의 최단거리 계산
    for i in range(len(edges)):
        for j in range(len(edges)):
            if i == j:
                continue
            for p in range(len(edges[i])):
                for q in range(len(edges[j])):
                    dis = abs(edges[i][p][0] - edges[j][q][0]) + \
                        abs(edges[i][p][1] - edges[j][q][1])-1
                    if dis < minN:
                        minN = dis

    print(minN)


sol()
