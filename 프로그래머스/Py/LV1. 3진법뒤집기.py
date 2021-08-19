# 단순 구현 . 3진법이므로 n==2 까지 넣어줘야한다

import math


def solution(n):
    tmp = ''
    res = 0

    while True:
        tmp += str(n % 3)
        if n == 1 or n == 0 or n == 2:
            break
        n //= 3

    for i in range(len(tmp)):
        res += int(tmp[i]) * math.pow(3, len(tmp)-i-1)

    return res
