# 풀이1 - 슬라이딩 윈도우


import sys


def solution(s):

    if len(s) == 1:
        return 1
    ans = -1e9

    # 길이 2 window - 길이 짝수
    for i in range(len(s)-1):
        lt1, rt1 = i, i+1
        if s[lt1] == s[rt1]:
            while True:
                if s[lt1] != s[rt1]:
                    break
                ans = max(ans, rt1-lt1+1)
                rt1 += 1
                lt1 -= 1
                if lt1 < 0 or rt1 > len(s)-1:
                    break

    # 길이 3 window - 길이 홀수
    for i in range(len(s)-2):
        lt2, rt2 = i, i+2
        if s[lt2] == s[rt2]:
            while True:
                if s[lt2] != s[rt2]:
                    break
                ans = max(ans, rt2-lt2+1)
                rt2 += 1
                lt2 -= 1
                if lt2 < 0 or rt2 > len(s)-1:
                    break

    if ans == -1e9:
        return 1
    else:
        return ans


# 풀이2 - 재귀
# 백트래킹 해줬는데도 효율성1 에서 TLE난다.

sys.setrecursionlimit(10**6)


def solution2(s):
    global res
    check = set()
    res = -1e9

    def recur(str):
        global res
        if str == "".join(str[::-1]):
            res = max(res, len(str))
            return
        if str[1:] not in check:
            check.add(str[1:])
            recur(str[1:])
        if str[:-1] not in check:
            check.add(str[:-1])
            recur(str[:-1])
    recur(s)
    return res
