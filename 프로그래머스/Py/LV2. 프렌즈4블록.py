# 시뮬레이션 문제
# 처음에 dfs, bfs로 헛짓거리해서 시간 다 날림
# 단순 브루트포스로 4개짜리 블록 구해주기 -> 중복된 블록이 있을 수 있으므로 set에 (값, 좌표) 튜플 형식으로 넣어주기
# 굳이 전치 행렬 사용하지 않아도 reset함수 적절히 구현하면 된다

def solution(m, n, board):
    grid = [list(b) for b in board]

    def reset(grid):  # 리셋함수 예전에 삼성문제에 써먹었던 것 -> n^2이라는 단점이 있음
        for i in range(n):
            tmp = []
            for j in range(m):
                if grid[j][i] != "-":
                    tmp.append(grid[j][i])
            for j in range(m - 1, -1, -1):
                if tmp:
                    grid[j][i] = tmp.pop()
                else:
                    grid[j][i] = "-"

    def bomb(grid):  # 폭파 함수 -> 인덱스 잘 조절하고 set에 넣어줘야함
        s = set()
        for i in range(m-1):
            for j in range(n-1):
                if grid[i][j] == grid[i][j+1] == grid[i+1][j+1] == grid[i+1][j] and grid[i][j] != "-":
                    s.add((grid[i][j], i, j))
                    s.add((grid[i][j+1], i, j+1))
                    s.add((grid[i+1][j+1], i+1, j+1))
                    s.add((grid[i+1][j], i+1, j))
        tmp_list = list(s)
        for i in range(len(tmp_list)):
            grid[tmp_list[i][1]][tmp_list[i][2]] = "-"

        return s

    while True:  # 시뮬레이션 -> set의 길이가 0이라는 것은 폭파할 블록이 없다는 것
        res_set = bomb(grid)
        if len(list(res_set)) == 0:
            break
        reset(grid)

    res = 0
    # 마지막에 "-" 갯수 카운팅해주면 된다
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "-":
                res += 1

    return res
