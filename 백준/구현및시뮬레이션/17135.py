# 골드4 - 캐슬디펜스
# 시뮬레이션 + DFS


# 예외처리가 너무 많아 반례 보고 맞췄다
# 시뮬레이션은 꼼꼼함이 관건...

import itertools as it

n, m, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
grid.append([0] * m)
archors = [(n, i) for i in range(m)]
max_cnt = -1e9

for tmp in it.combinations(archors, 3):
    # 배열 복사
    copy = [layer[:] for layer in grid]
    enemy_die_cnt = 0

    while True:
        # 궁수 배치 & 사격
        final_enemy = set()
        for t in tmp:
            x, y = t
            copy[x][y] = -1

            # 공격 - 각 궁수 마다
            avail = []  # 각 궁수마다 사격 가능한 적 위치들

            for i in range(n):
                for j in range(m):
                    if copy[i][j] == 1 and abs(x - i) + abs(y - j) <= d:
                        avail.append((abs(x - i) + abs(y - j), i, j))
            avail.sort(key=lambda s: (s[0], s[2]))

            if avail:
                final_enemy.add((avail[0][1], avail[0][2]))
        final_enemy = list(final_enemy)

        for f in final_enemy:
            nx, ny = f[0], f[1]
            copy[nx][ny] = 0
            enemy_die_cnt += 1

        # 모든 적이 죽으면 종료
        die = 0
        for i in range(n):
            for j in range(m):
                if copy[i][j] == 0:
                    die += 1
        if die == n * m:
            break

        # 적 이동
        castle_destroy = False
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(copy[j][i])
            pop = arr.pop()
            arr.insert(0, 0)
            for j in range(n):
                copy[j][i] = arr[j]

    max_cnt = max(max_cnt, enemy_die_cnt)

print(max_cnt)
