# 실버4-요세푸스
# 특별한건 없고 join함수 잘 기억하기

import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
q = deque(list(range(1, n+1)))
cnt = 1
tmp = []

while q:
    curr = q.popleft()
    if cnt % k != 0:
        q.append(curr)
    else:
        tmp.append(str(curr))
    cnt += 1


print("<", ", ".join(tmp), ">", sep="")
