# 큐 이용
# idx 라는 변수로 큐와 speeds 배열의 인덱스를 맞춰주었음

from collections import deque


def solution(progresses, speeds):

    q = deque(progresses)
    cnt = 0
    idx = 0
    res = []
    timer = 1
    while q:
        if q[0] >= 100:
            while q and q[0] >= 100:
                q.popleft()
                idx += 1
                cnt += 1
        if cnt > 0:
            res.append(cnt)
            cnt = 0
        for i in range(len(q)):
            q[i] += speeds[idx+i]
        timer += 1

    return res
