# 단순 구현

def solution(N, stages):
    arr = sorted(stages)
    acc = 0
    tmp = []
    for i in range(1, N+1):
        cnt = 0
        for j in range(len(arr)):
            if arr[j] == i:
                cnt += 1
        if cnt != 0:
            tmp.append((i, cnt/(len(stages)-acc)))
        else:
            tmp.append((i, 0))
        acc += cnt
    tmp.sort(key=lambda x: -x[1])
    res = []
    for t in tmp:
        res.append(t[0])

    return res
