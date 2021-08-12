# 골드2 - 통나무 옮기기
# BFS


from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

btree = []
etree = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == "B":
            btree.append((i, j))
        if grid[i][j] == "E":
            etree.append((i, j))


def bfs(arr):
    q = deque()
    q.append(arr)
    check = set()
    check.add(tuple(arr))
    level = 0
    while q:
        # print(q)
        for _ in range(len(q)):
            qarr = q.popleft()
            if sorted(qarr, key=lambda x: (x[0], x[1])) == sorted(etree, key=lambda x: (x[0], x[1])):
                return level
            t1, t2, t3 = qarr[0], qarr[1], qarr[2]

            for s in range(6):
                if s == 4:  # 오른 회전
                    # 세로방향이면
                    if t1[1] - t2[1] == 0:
                        if 0 <= t1[0] <= n - 1 and 0 <= t1[1] + 1 <= n - 1:
                            if grid[t1[0]][t1[1] + 1] == "1":
                                continue
                        if 0 <= t3[0] <= n - 1 and 0 <= t3[1] - 1 <= n - 1:
                            if grid[t3[0]][t3[1] - 1] == "1":
                                continue
                        t1x, t1y = t1[0] + 1, t1[1] + 1
                        t2x, t2y = t2[0], t2[1]
                        t3x, t3y = t3[0] - 1, t3[1] - 1
                        res = ((t1x, t1y), (t2x, t2y), (t3x, t3y))
                        res = tuple(sorted(res, key=lambda x: (x[0], x[1])))
                        if all(
                                0 <= tmp[0] <= n - 1 and 0 <= tmp[1] <= n - 1 and (
                                    grid[tmp[0]][tmp[1]] == "0" or grid[tmp[0]][tmp[1]] == "E" or grid[tmp[0]][
                                        tmp[1]] == "B")
                                for tmp in res) and res not in check:
                            q.append(res)
                            check.add(res)

                    # 가로방향이면
                    else:
                        # continue 조건 넣으면 된다.
                        if 0 <= t1[0] - 1 <= n - 1 and 0 <= t1[1] <= n - 1:
                            if grid[t1[0] - 1][t1[1]] == "1":
                                continue
                        if 0 <= t3[0] + 1 <= n - 1 and 0 <= t3[1] <= n - 1:
                            if grid[t3[0] + 1][t3[1]] == "1":
                                continue
                        t1x, t1y = t1[0] - 1, t1[1] + 1
                        t2x, t2y = t2[0], t2[1]
                        t3x, t3y = t3[0] + 1, t3[1] - 1
                        res = ((t1x, t1y), (t2x, t2y), (t3x, t3y))
                        res = tuple(sorted(res, key=lambda x: (x[0], x[1])))
                        if all(
                                0 <= tmp[0] <= n - 1 and 0 <= tmp[1] <= n - 1 and (
                                    grid[tmp[0]][tmp[1]] == "0" or grid[tmp[0]][tmp[1]] == "E" or grid[tmp[0]][
                                        tmp[1]] == "B")
                                for tmp in res) and res not in check:
                            q.append(res)
                            check.add(res)

                elif s == 5:  # 왼 회전
                    # 세로방향이면
                    if t1[1] - t2[1] == 0:
                        if 0 <= t1[0] <= n - 1 and 0 <= t1[1] - 1 <= n - 1:
                            if grid[t1[0]][t1[1] - 1] == "1":
                                continue
                        if 0 <= t3[0] <= n - 1 and 0 <= t3[1] + 1 <= n - 1:
                            if grid[t3[0]][t3[1] + 1] == "1":
                                continue
                        t1x, t1y = t1[0] + 1, t1[1] - 1
                        t2x, t2y = t2[0], t2[1]
                        t3x, t3y = t3[0] - 1, t3[1] + 1
                        res = ((t1x, t1y), (t2x, t2y), (t3x, t3y))
                        res = tuple(sorted(res, key=lambda x: (x[0], x[1])))
                        if all(
                                0 <= tmp[0] <= n - 1 and 0 <= tmp[1] <= n - 1 and (
                                    grid[tmp[0]][tmp[1]] == "0" or grid[tmp[0]][tmp[1]] == "E" or grid[tmp[0]][
                                        tmp[1]] == "B")
                                for tmp in res) and res not in check:
                            q.append(res)
                            check.add(res)

                    # 가로방향이면
                    else:
                        # continue 조건 넣으면 된다.
                        if 0 <= t1[0] + 1 <= n - 1 and 0 <= t1[1] <= n - 1:
                            if grid[t1[0] + 1][t1[1]] == "1":
                                continue
                        if 0 <= t3[0] - 1 <= n - 1 and 0 <= t3[1] <= n - 1:
                            if grid[t3[0] - 1][t3[1]] == "1":
                                continue
                        t1x, t1y = t1[0] + 1, t1[1] + 1
                        t2x, t2y = t2[0], t2[1]
                        t3x, t3y = t3[0] - 1, t3[1] - 1
                        res = ((t1x, t1y), (t2x, t2y), (t3x, t3y))
                        res = tuple(sorted(res, key=lambda x: (x[0], x[1])))
                        if all(
                                0 <= tmp[0] <= n - 1 and 0 <= tmp[1] <= n - 1 and (
                                    grid[tmp[0]][tmp[1]] == "0" or grid[tmp[0]][tmp[1]] == "E" or grid[tmp[0]][
                                        tmp[1]] == "B")
                                for tmp in res) and res not in check:
                            q.append(res)
                            check.add(res)

                else:  # 위 아래 왼 오
                    t1x, t1y = t1[0] + dx[s], t1[1] + dy[s]
                    t2x, t2y = t2[0] + dx[s], t2[1] + dy[s]
                    t3x, t3y = t3[0] + dx[s], t3[1] + dy[s]
                    # print(s, (t1x,t1y),(t2x,t2y),(t3x,t3y))
                    res = ((t1x, t1y), (t2x, t2y), (t3x, t3y))
                    res = tuple(sorted(res, key=lambda x: (x[0], x[1])))
                    if all(
                            0 <= tmp[0] <= n - 1 and 0 <= tmp[1] <= n - 1 and (
                                grid[tmp[0]][tmp[1]] == "0" or grid[tmp[0]][tmp[1]] == "E" or grid[tmp[0]][
                                    tmp[1]] == "B")
                            for tmp in res) and res not in check:
                        q.append(res)
                        check.add(res)
        level += 1
    return 0


print(bfs(tuple(btree)))
