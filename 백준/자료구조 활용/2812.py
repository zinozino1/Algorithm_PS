# 골드5-스택-크게만들기
# 스택 빡세게 구현

import heapq
import sys
input = sys.stdin.readline


def sol():

    n, k = map(int, input().split())
    target = list(map(int, input().rstrip()))
    stack = []

    # 문자열 각 숫자마다 작업시작
    for t in target:
        # 스택에 넣기전 이미 스택에 들어가 있는 원소들과 비교하여 넣으려는 값보다 작으면 pop해주고
        # 숫자 삭제 카운트 하나 감소 시킴
        while stack and stack[-1] < t and k > 0:
            stack.pop()
            k -= 1
        stack.append(t)

    res = ''
    # 삭제 카운트가 남아 있는 경우 stack 끝에서부터 차례로 제거해주면 된다
    for x in stack[:len(stack)-k]:
        res += str(x)

    print(res)


sol()
