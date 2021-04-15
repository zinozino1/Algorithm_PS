# DFS/BFS 완전탐색


import copy
import sys
from collections import deque

limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline


def sol():

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def next_pos(pos, dir):
        ndx = [0, -1, 0, 1, 0]
        ndy = [0, 0, 1, 0, -1]
        pos[0] = pos[0] + ndx[dir % 5]
        pos[1] = pos[1] + ndy[dir % 5]
        return pos

    def bfs(x, y, c, p):
        q = deque()
        q.append((x, y))
        check = [[0]*10 for _ in range(10)]

        check[x][y] = 1

        cnt = 0
        while q:
            if cnt == c+1:
                break
            for _ in range(len(q)):
                curr = q.popleft()
                if grid[curr[0]][curr[1]] != [0]:
                    grid[curr[0]][curr[1]].append(p)
                else:
                    grid[curr[0]][curr[1]] = [p]
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= 9 and 0 <= ny <= 9 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        q.append((nx, ny))
            cnt += 1

    t = int(input())
    test_case = 1
    for _ in range(t):
        m, a = map(int, input().split())  # m : move_distance a : ap 개수
        move_a = list(map(int, input().split()))
        move_b = list(map(int, input().split()))

        grid = [[[0] for _ in range(10)] for _ in range(10)]

        for _ in range(a):
            x, y, c, p = map(int, input().split())
            bfs(y-1, x-1, c, p)

        for s in grid:
            print(s)
        print()

        a_pos = [0, 0]
        b_pos = [9, 9]
        a_charge = 0
        b_charge = 0

        for i in range(m+1):

            if len(grid[a_pos[0]][a_pos[1]]) == 1 and len(grid[b_pos[0]][b_pos[1]]) == 1:
                a_charge += grid[a_pos[0]][a_pos[1]][0]
                b_charge += grid[b_pos[0]][b_pos[1]][0]

            else:
                max_charge_capa = -1e9
                max_charge_a = -1e9
                max_charge_b = -1e9
                for s in range(len(grid[a_pos[0]][a_pos[1]])):
                    for k in range(len(grid[b_pos[0]][b_pos[1]])):
                        if grid[a_pos[0]][a_pos[1]][s] == grid[b_pos[0]][b_pos[1]][k]:
                            if max_charge_capa < grid[a_pos[0]][a_pos[1]][s]:
                                max_charge_capa = grid[a_pos[0]][a_pos[1]][s]
                                max_charge_a = grid[a_pos[0]][a_pos[1]][s]
                                max_charge_b = grid[a_pos[0]][a_pos[1]][s]
                        else:
                            if grid[a_pos[0]][a_pos[1]][s] + grid[b_pos[0]][b_pos[1]][k] > max_charge_capa:
                                max_charge_capa = grid[a_pos[0]][a_pos[1]
                                                                 ][s] + grid[b_pos[0]][b_pos[1]][k]
                                max_charge_a = grid[a_pos[0]][a_pos[1]][s]
                                max_charge_b = grid[b_pos[0]][b_pos[1]][k]
                a_charge += max_charge_a
                b_charge += max_charge_b

            # 방향 입력 받고 다음 위치 구하는 함수
            if i >= m:
                break
            a_pos = next_pos(a_pos, move_a[i])
            b_pos = next_pos(b_pos, move_b[i])
            # print("a 누적 : ",a_charge)
            # print("b 누적 : ",b_charge)

        print("#%d %d" % (test_case, a_charge+b_charge))

        test_case += 1


sol()
