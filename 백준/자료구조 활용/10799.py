# 실버3-쇠막대기
# 스택 활용

import sys
from collections import deque
input = sys.stdin.readline


target = input().strip()
stack = []
res = 0
cnt = 0

for t in target:
    if t == "(":
        stack.append(t)
        cnt += 1
    else:
        if stack and stack[-1] == "(":
            stack.pop()
            cnt -= 1
            res += cnt
        elif stack and stack[-1] == ")":
            cnt -= 1
            res += 1
        stack.append(t)

print(res)
