# 실버1 - 상어초등학교
# 구현

# 삼성기출이다..
# 다시 푸니 30분걸림

n = int(input())
student = [tuple(map(int, input().split())) for _ in range(n*n)]
grid = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dic = {}

for s in student:
    sn = s[0]
    like = [s[1], s[2], s[3], s[4]]
    dic[sn] = like
    candi = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                empty_cnt = 0
                likes_cnt = 0
                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if 0 <= ni <= n-1 and 0 <= nj <= n-1 and grid[ni][nj] == 0:
                        empty_cnt += 1
                    if 0 <= ni <= n-1 and 0 <= nj <= n-1 and grid[ni][nj] in like:
                        likes_cnt += 1
                candi.append((likes_cnt, empty_cnt, i, j))

    candi.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    targetx, targety = candi[0][2], candi[0][3]
    grid[targetx][targety] = sn

score = 0
for i in range(n):
    for j in range(n):
        target = grid[i][j]
        cnt = 0
        for s in range(4):
            ni = i+dx[s]
            nj = j+dy[s]
            if 0 <= ni <= n-1 and 0 <= nj <= n-1 and grid[ni][nj] in dic[grid[i][j]]:
                cnt += 1
        if cnt == 1:
            score += 1
        elif cnt == 2:
            score += 10
        elif cnt == 3:
            score += 100
        elif cnt == 4:
            score += 1000

print(score)
