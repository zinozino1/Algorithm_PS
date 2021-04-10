# 골드4-스택-후위표기식
# 넣기전에 검사한다는 것만 명심


import heapq
import sys
input = sys.stdin.readline


def sol():

    target = list(input().rstrip())

    stack = []
    res = ''

    for x in target:

        # 알파벳일 경우 그냥 넣기
        if x.isalpha():
            stack.append(x)

            # +,- 일경우 *,/ 보다 순위 낮으므로 ( 제외하고 넣기전에 모두(알파벳,+,-,*,/) 꺼내야함
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)

            # *,/ 일경우 +,- 보다 순위 높으므로 +,- 만나기전에 브레이크, ( 는 당연히 브레이크
        elif x == "*" or x == "/":
            while stack and stack[-1] != "(" and stack[-1] != "+" and stack[-1] != "-":
                res += stack.pop()
            stack.append(x)

        elif x == "(":
            stack.append(x)
            # ) 일경우 ( 만날때까지 모두 pop
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

            # 남은 것들 정답에 합치기
    while stack:
        res += stack.pop()

    print(res)


sol()
