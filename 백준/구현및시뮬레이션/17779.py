# 골드4-게리맨더링
# 하라는대로 하면 된다
# 좌표 헷갈릴 거 같으면 그냥 +1 붙여서 평면 만들어버리자 안하면 괜히 헷갈림
# 수학적 수식을 계산하는 문제는 안 나오니 수식이 나오면 쫄지말고 그대로 구현해

import copy
from collections import deque
import itertools as it

# 17:40


def sol():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    for g in grid:
        g.insert(0, 0)
        g.append(0)
    grid.insert(0, [0]*(n+2))
    grid.append([0]*(n+2))

    min_diff = 1e9

    for i in range(1, n+1):
        for j in range(1, n+1):
            x, y = i, j

            candidate = []
            for d1 in range(1, n+1):
                for d2 in range(1, n+1):
                    if 1 <= x <= x+d1+d2 <= n and 1 <= y-d1 <= y < y+d2 <= n:
                        candidate.append((d1, d2))

            if not candidate:
                continue
            # 경계선 세우기

            for c in candidate:
                check = [[0] * (n+2) for _ in range(n+2)]
                nd1, nd2 = c[0], c[1]

                for s in range(nd1+1):
                    # 1, 4
                    check[x + s][y - s] = 5
                    check[x + nd2 + s][y + nd2 - s] = 5

                for s in range(nd2+1):
                    # 2, 4
                    check[x + s][y + s] = 5
                    check[x + nd1 + s][y - nd1 + s] = 5

                for s in range(1, n+1):
                    flag = False
                    if check[s].count(5) == 1:
                        continue
                    for z in range(1, n+1):
                        if not flag:
                            if check[s][z] == 5:
                                flag = True
                        else:
                            if check[s][z] == 5:
                                break
                            check[s][z] = 5

                for p in range(1, n+1):
                    for q in range(1, n+1):
                        # 1
                        if 1 <= p < x+nd1 and 1 <= q <= y:
                            if check[p][q] == 5:
                                continue
                            check[p][q] = 1
                        # 2
                        elif 1 <= p <= x+nd2 and y < q <= n:
                            if check[p][q] == 5:
                                continue
                            check[p][q] = 2
                        # 3
                        elif x+nd1 <= p <= n and 1 <= q < y-nd1+nd2:
                            if check[p][q] == 5:
                                continue
                            check[p][q] = 3
                        # 4
                        elif x+nd2 < p <= n and y-nd1+nd2 <= q <= n:
                            if check[p][q] == 5:
                                continue
                            check[p][q] = 4

                s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
                for p in range(1, n+1):
                    for q in range(1, n+1):
                        if check[p][q] == 1:
                            s1 += grid[p][q]
                        elif check[p][q] == 2:
                            s2 += grid[p][q]
                        elif check[p][q] == 3:
                            s3 += grid[p][q]
                        elif check[p][q] == 4:
                            s4 += grid[p][q]
                        elif check[p][q] == 5:
                            s5 += grid[p][q]

                if max(s1, s2, s3, s4, s5) - min(s1, s2, s3, s4, s5) < min_diff:
                    min_diff = max(s1, s2, s3, s4, s5) - \
                        min(s1, s2, s3, s4, s5)

    print(min_diff)


sol()
