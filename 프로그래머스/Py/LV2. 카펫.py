# 완전 탐색

def solution(brown, yellow):
    target = brown + yellow

    for i in range(1, target+1):
        if target % i == 0 and i >= target // i and (i-2)*((target // i) - 2) == yellow:
            return [i, target // i]
