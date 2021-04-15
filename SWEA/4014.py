# 기본 구현 및 시뮬레이션


from collections import deque
import sys
T = int(input())


def possible(arr, x):
    cnt = 1
    bef = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < bef:  # 내리막
            if bef-arr[i] > 1:
                return 0
            else:
                if i+x > len(arr):
                    return 0
                else:
                    for j in range(i, i+x):  # 앞을 본다
                        if arr[j] != arr[i]:
                            return 0
                    cnt = -x+1  # 개어렵네
        elif arr[i] > bef:  # 오르막
            if arr[i]-bef > 1:
                return 0
            else:
                if cnt >= x:
                    cnt = 1
                else:
                    return 0
        # 평지
        else:
            cnt += 1
        bef = arr[i]
    return 1


for test in range(T):
    N, X = map(int, input().split())
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())))
    sol = 0
    # 가로
    for i in mat:
        sol += possible(i, X)
    # 세로
    for i in zip(*mat):  # 전치행렬
        sol += possible(i, X)
    print('#%d' % (test+1), sol)


# 내코드


# 17:00

input = sys.stdin.readline


def sol():

    t = int(input())

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    num = 1

    for _ in range(t):
        n, x = map(int, input().split())

        grid = [list(map(int, input().split())) for _ in range(n)]

        removed_col = {}
        removed_row = {}
        check = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for s in range(4):
                    nx = i+dx[s]
                    ny = j+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                        # 크거나 같은 경우
                        if grid[i][j] >= grid[nx][ny]:
                            pass

                        # 작은 경우
                        else:
                            # 높이가 1이상인 경우
                            if grid[nx][ny] - grid[i][j] > 1:
                                check = [[0]*n for _ in range(n)]
                                # 가로냐 세로냐
                                print((i, j))
                                if (nx, ny) == (i, j-1) or (nx, ny) == (i, j+1):
                                    print("가로가 문제", i)
                                    removed_row[i] = 1
                                elif (nx, ny) == (i-1, j) or (nx, ny) == (i+1, j):
                                    print("세로가 문제", j)
                                    removed_col[j] = 1
                            # 높이가 1인 경우 뒤에거 봐야함
                            else:

                                flag = True
                                cnt = 0
                                #tmp = []
                                for q in range(x):
                                    # grid 벗어나는 경우
                                    if i+dx[s]*-q > n-1 or i+dx[s]*-q < 0 or j+dy[s]*-q > n-1 or j+dy[s]*-q < 0:
                                        flag = False
                                        break
                                    if grid[i][j] == grid[i+dx[s]*-q][j+dy[s]*-q] and check[i+dx[s]*-q][j+dy[s]*-q] == 0:
                                        check[i+dx[s]*-q][j+dy[s]*-q] = 1
                                        #tmp.append((i+dx[s]*-q, j+dy[s]*-q))
                                        cnt += 1
                                # 경사로 가로 길이 만족 못하는 경우
                                if cnt != x:
                                    flag = False
                                    check = [[0]*n for _ in range(n)]
                                # else:
                                #   for p in tmp:
                                #     check[p[0]][p[1]] = 1
                                # for l in check:
                                #   print(l)
                                # print()

                                if not flag:
                                    print((i, j))
                                    if (nx, ny) == (i, j - 1) or (nx, ny) == (i, j + 1):
                                        print("가로가 문제", i)
                                        removed_row[i] = 1
                                    elif (nx, ny) == (i - 1, j) or (nx, ny) == (i + 1, j):
                                        print("세로가 문제", j)
                                        removed_col[j] = 1

        print("col", removed_col)
        print("row", removed_row)

        print("#%d %d" % (num, 2*n-(len(removed_col)+len(removed_row))))

        num += 1


sol()
