# ㅈㄴ게 어렵네

def solution(n):

    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            print(i, j)
            if i % 3 == 0:
                x += 1  # 아래
            elif i % 3 == 1:
                y += 1  # 옆
            elif i % 3 == 2:
                x -= 1  # 대각
                y -= 1
            res[x][y] = num
            num += 1
        for r in res:
            print(r)
        print()
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer
