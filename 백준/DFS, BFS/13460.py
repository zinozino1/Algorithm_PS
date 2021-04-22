# 골드2-구슬탈출2
# BFS 돌리면서 가능한 모든 빨간구슬, 파란구슬 좌표를 넣고,
# move를 통해 가능한 좌표 모두 구하고 큐에 넣는다
# 이때 이미 방문한 좌표라면 큐에 넣지 않음
# 구현하기 쉽게 visited를 일차원 리스트로


import copy
from collections import deque
import itertools as it

# 11:05


def sol():
    def move(i, j, di, dj):
        cnt = 0
        while board[i+di][j+dj] != "#" and board[i][j] != "O":
            i += di
            j += dj
            cnt += 1
        return i, j, cnt

    def simulation(ri, rj, bi, bj, d):

        q = deque()
        q.append((ri, rj, bi, bj, d))
        visited.append((ri, rj, bi, bj))

        while q:
            for _ in range(len(q)):
                sri, srj, sbi, sbj, sd = q.popleft()

                # 10번 넘어가면 리턴
                if sd > 10:
                    return -1

                for s in range(4):

                    # 좌표 변환 후 큐에 넣기

                    nri, nrj, rcnt = move(sri, srj, dx[s], dy[s])
                    nbi, nbj, bcnt = move(sbi, sbj, dx[s], dy[s])

                    # 파란구슬이 들어가면 안된다
                    if board[nbi][nbj] != "O":
                        if board[nri][nrj] == "O":
                            # 이거 자체가 최소값 출력과 동일
                            return sd
                        if nri == nbi and nrj == nbj:
                            if rcnt > bcnt:
                                nri -= dx[s]
                                nrj -= dy[s]
                            else:
                                nbi -= dx[s]
                                nbj -= dy[s]

                        if (nri, nrj, nbi, nbj) not in visited:
                            visited.append((nri, nrj, nbi, nbj))
                            q.append((nri, nrj, nbi, nbj, sd+1))

        # 빨간구슬이 구멍에 안들어가는 경우
        return -1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    ri, rj, bi, bj = -1, -1, -1, -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                ri, rj = i, j
            if board[i][j] == "B":
                bi, bj = i, j

    visited = []
    res = simulation(ri, rj, bi, bj, 1)
    print(res)


sol()
