# 큐 활용
# 매우 무난한 문제

from collections import deque


def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        if i == location:
            q.append((priorities[i], 1))
        else:
            q.append((priorities[i], 0))
    cnt = 1
    while q:
        flag = False
        curr = q.popleft()
        for i in range(len(q)):
            if q[i][0] > curr[0]:
                flag = True
        if flag:
            q.append(curr)
        else:
            if curr[1] == 1:
                return cnt
            else:
                cnt += 1
            flag = False
