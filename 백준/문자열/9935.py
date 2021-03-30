# 골드4-문자열-문자열폭탄
# replace로 했다가 시간초과났음
# 연속된 문자열 -> 재귀 vs 스택
# 스택을 선택해서 품

import sys
input = sys.stdin.readline


def sol():

    target = input().strip()
    bomb = input().strip()
    stack = []

    for i in range(len(target)):
        stack.append(target[i])

        # stack에 원소 추가될 때마다 스택 맨 위부터 bomb의 길이만큼 검사
        if len(stack[len(stack)-len(bomb):len(stack)]) == len(bomb):
            tmp = "".join(stack[len(stack)-len(bomb):len(stack)])
            # 만약 같으면 stack에서 bomb 길이만큼 pop
            if tmp == bomb:
                bomb_cnt = 0
                while stack:
                    if bomb_cnt == len(bomb):
                        break
                    stack.pop()
                    bomb_cnt += 1
    # 문자열 모두 폭파
    if not stack:
        print("FRULA")
    # 남아있는 문자 존재
    else:
        print("".join(stack))


sol()
