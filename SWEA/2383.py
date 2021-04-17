# DFS/BFS 완전탐색
# re try gg

import copy
import sys
from collections import deque

limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline


def sol():
    global min_time

    def simulation(peoples, steps_capa):
        max_time = -1e9

        q_arr = []
        while True:

            for i in range(len(steps)):
                q_arr.append(deque())

            for p in range(len(peoples)):
                for s in range(len(steps)):
                    if steps[s][0] == peoples[p][2] and steps[s][1] == peoples[p][3]:
                        q_arr[s].append(peoples[p])

            for i in range(len(q_arr)):
                tmp = []
                while q_arr[i]:
                    curr = q_arr[i].popleft()
                    dis = abs(curr[2]-curr[0])+abs(curr[3]-curr[1])
                    tmp.append(dis)
                tmp.sort()
                q_arr[i] = deque(tmp)

            for i in range(len(q_arr)):
                time = 0
                step_in_capa = 3
                step_out_capa = 3
                sc = steps_capa[i]
                while q_arr[i]:
                    # 계단 입구에서 기다리기
                    if q_arr[i][0] == time:
                        while q_arr[i][0] <= time and step_out_capa != 0:
                            q_arr[i].popleft()
                            step_out_capa -= 1

                if time > max_time:
                    max_time = time

            #max_time += 1

            print(q_arr)

        return 1

    def dfs(L, peoples, steps, steps_capa):
        global min_time

        if L == len(peoples):
            # for x in peoples:
            #   print(x)
            # print()
            time = simulation(peoples, steps_capa)
            if time < min_time:
                min_time = time
            return
        else:
            for s in range(len(steps)):
                peoples[L].append(steps[s][0])
                peoples[L].append(steps[s][1])
                dfs(L+1, peoples, steps, steps_capa)
                peoples[L].pop()
                peoples[L].pop()

    t = int(input())

    for _ in range(t):
        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(n)]

        peoples = []
        steps = []
        steps_capa = []
        min_time = 1e9
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    peoples.append([i, j])
                else:
                    if grid[i][j] != 0:
                        steps.append([i, j])

        dfs(0, peoples, steps, steps_capa)


sol()
