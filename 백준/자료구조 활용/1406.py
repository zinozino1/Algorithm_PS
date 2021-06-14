# 실버3-에디터
# 스택
# 시간복잡도를 줄이기 위해 스택 두개를 사용한다
# 타겟스택의 top이 커서의 역할을 함
# o(n)으로 해결가능

import sys
input = sys.stdin.readline


target_stack = list(input().strip())
second_stack = []

n = int(input())

for _ in range(n):
    order = input().split()
    if order[0] == "L":
        if target_stack:
            second_stack.append(target_stack.pop())
    elif order[0] == "D":
        if second_stack:
            target_stack.append(second_stack.pop())
    elif order[0] == "B":
        if target_stack:
            target_stack.pop()
    else:
        target_stack.append(order[1])

res = ''

for x in target_stack:
    res += x
for i in range(len(second_stack)-1, -1, -1):
    res += second_stack[i]

print(res)

