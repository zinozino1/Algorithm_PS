# 골드5 - 치킨배달
# DFS

import itertools as it

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

chikens = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            chikens.append((i, j))

global_min = 1e9
for tmp in it.combinations(chikens, m):
    total_dis = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                min_dis = 1e9
                for t in tmp:
                    x, y = t
                    min_dis = min(min_dis, abs(i-x)+abs(j-y))
                total_dis += min_dis
    global_min = min(global_min, total_dis)
print(global_min)
