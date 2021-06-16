# 실버3-단어뒤집기
# 이런건 쉽게 풀어야하지 않을까 진호야?
# 큐와 스택 사용


import sys
from collections import deque
input = sys.stdin.readline


target = input().strip()

q = deque(list(target))
s = []
res = ''
flag = False

while q:
    curr = q.popleft()

    if curr == "<":
        if s:
            tmp = ''
            while s:
                tmp += s.pop()
            res += tmp
        flag = True
        res += curr
        continue
    elif curr == ">":
        flag = False
        res += curr
        continue

    if curr == " " and not flag:
        if s:
            tmp = ''
            while s:
                tmp += s.pop()
            res += tmp
        res += curr
        continue

    if flag:
        res += curr
    else:
        s.append(curr)


if s:
    while s:
        res += s.pop()

print(res)
