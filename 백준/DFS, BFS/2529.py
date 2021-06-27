# 실버2-부등호
# 하 오래걸림 ㅈ밥 문젠데
# DFS + 백트래킹이 관건 -> 부등호를 만족하지 않는 순간에 바로 리턴

import itertools as it
n = int(input())
target = input().split()
minN, maxN = 1e11, -1e11
min_str, max_str = '', ''


def check(str, L):
    tmp = ''
    correct_cnt = 0
    for i in range(len(str)):
        if i <= len(str)-2:
            tmp += str[i]
            tmp += target[i]
        else:
            tmp += str[i]

    for i in range(0, len(tmp)-2, 2):
        if eval(tmp[i:i+3]):
            correct_cnt += 1

    if correct_cnt == L-1:
        return True
    else:
        return False


def dfs(L, res, type):
    global minN, maxN, min_str, max_str
    if L > 1 and not check(res, L):
        return
    # back tracking
    if type == "max" and max_str and int(res[:L]) < int(max_str[:L]):
        return
    elif type == "min" and min_str and int(res[:L]) > int(min_str[:L]):
        return
    if L == len(target)+1:
        if type == "max" and int(res) > maxN:
            maxN, max_str = int(res), res
        if type == "min" and int(res) < minN:
            minN, min_str = int(res), res
        return
    else:
        if type == "min":
            for i in range(10):
                if check_arr[i] == 0:
                    check_arr[i] = 1
                    dfs(L+1, res+str(i), type)
                    check_arr[i] = 0
        else:
            for i in range(9, -1, -1):
                if check_arr[i] == 0:
                    check_arr[i] = 1
                    dfs(L+1, res+str(i), type)
                    check_arr[i] = 0


check_arr = [0]*10
dfs(0, '', "max")
dfs(0, '', "min")

print(max_str)
print(min_str)
