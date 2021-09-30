from collections import deque


def bfs(x, y, visited, place):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    level = 0

    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[nx][ny] == 0 and place[nx][ny] == "P" and level <= 1:
                    return False
                if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[nx][ny] == 0 and place[nx][ny] == "O":
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        level += 1
    return True


def solution(places):
    n = 5
    res = []
    for place in places:
        copied = []
        for p in place:
            copied.append(list(p))
        for i in range(n):
            flag = False
            for j in range(n):
                visited = [[0]*5 for _ in range(5)]
                if copied[i][j] == "P":
                    if not bfs(i, j, visited, copied):
                        res.append(0)
                        flag = True
                        break
            if flag:
                break
        else:
            res.append(1)

    return res
