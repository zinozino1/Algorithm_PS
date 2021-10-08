# 분할정복


def solution(arr):
    global zero, one
    zero, one = 0, 0
    n = len(arr)

    def recur(x, y, n):
        global zero, one
        flag = False
        zero_cnt = 0
        one_cnt = 0
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] == 0:
                    zero_cnt += 1
                elif arr[i][j] == 1:
                    one_cnt += 1

        if zero_cnt == n*n:
            flag = True
            zero += 1
        if one_cnt == n*n:
            flag = True
            one += 1

        if not flag:
            recur(x+n//2, y, n//2)
            recur(x, y+n//2, n//2)
            recur(x+n//2, y+n//2, n//2)
            recur(x, y, n//2)

    recur(0, 0, n)
    return [zero, one]
