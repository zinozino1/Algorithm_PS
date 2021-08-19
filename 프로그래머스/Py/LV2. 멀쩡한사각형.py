# 코딩문제라기보단 수학 테스트같은 느낌..
# math 라이브러리를 이용하여 최대공약수를 구할 수 있음

import math


def solution(w, h):
    return w*h - (w+h-math.gcd(w, h))
