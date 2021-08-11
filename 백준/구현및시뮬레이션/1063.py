# 실버4 - 킹
# 구현

# 세심함이 필요

pos = list(input().split())
n = int(pos[2])
dir = {"R": 0, "L": 2, "B": 1, "T": 3, "RT": 7, "RB": 4, "LB": 5, "LT": 6}
posdic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
posdic2 = {"0": "A", "1": "B", "2": "C", "3": "D",
           "4": "E", "5": "F", "6": "G", "7": "H"}
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
kingx, kingy = 8-int(pos[0][1]), posdic[pos[0][0]]
stonex, stoney = 8-int(pos[1][1]), posdic[pos[1][0]]

grid = [[0]*8 for _ in range(8)]
grid[kingx][kingy] = 1
grid[stonex][stoney] = 2

for i in range(n):
    od = input().strip()
    idx = dir[od]

    knx, kny = kingx+dx[idx], kingy+dy[idx]

    if not (0 <= knx <= 7 and 0 <= kny <= 7):
        continue
    # 앞에 돌이 있다면
    if grid[knx][kny] == 2:
        snx, sny = stonex+dx[idx], stoney+dy[idx]

        if not (0 <= knx <= 7 and 0 <= kny <= 7) or not (0 <= snx <= 7 and 0 <= sny <= 7):
            continue

        grid[stonex][stoney] = 0
        stonex, stoney = snx, sny
        grid[stonex][stoney] = 2

        grid[kingx][kingy] = 0
        kingx, kingy = knx, kny
        grid[kingx][kingy] = 1

    # 앞에 돌이 없다면
    else:
        if not (0 <= knx <= 7 and 0 <= kny <= 7):
            continue
        else:
            grid[kingx][kingy] = 0
            kingx, kingy = knx, kny
            grid[kingx][kingy] = 1

final = []
for i in range(8):
    for j in range(8):
        if grid[i][j] == 1:
            res1 = ''
            res1 += posdic2[str(j)]+str(8-i)
            final.append(res1)
for i in range(8):
    for j in range(8):
        if grid[i][j] == 2:
            res2 = ''
            res2 += posdic2[str(j)]+str(8-i)
            final.append(res2)

print(final[0])
print(final[1])
