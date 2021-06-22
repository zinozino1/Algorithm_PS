def solution(left, right):
    curr = left
    res = 0
    while curr <= right:
        cnt = 0
        for i in range(1, curr+1):
            if curr % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            res += curr
        else:
            res -= curr
        curr += 1

    return res
