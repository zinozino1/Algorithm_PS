# dfs + stack 응용
import itertools as it


def solution(expression):

    res = -1e9

    target = []
    operand = set()
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            target.append(tmp)
            tmp = ''
            target.append(e)
            operand.add(e)
    target.append(tmp)
    available = []

    for p in it.permutations(operand, len(operand)):
        available.append(p)

    for i in range(len(available)):
        stack = target[::-1]
        tmp = []
        for j in range(len(available[i])):

            while stack:
                curr = stack.pop()
                if stack and stack[-1] == available[i][j]:
                    curr2 = stack.pop()
                    curr3 = stack.pop()

                    if curr2 == "+":
                        local = str(int(curr)+int(curr3))
                        stack.append(local)
                    elif curr2 == "-":
                        local = str(int(curr)-int(curr3))
                        stack.append(local)
                    elif curr2 == "*":
                        local = str(int(curr)*int(curr3))
                        stack.append(local)
                else:
                    tmp.append(curr)

            if len(tmp) == 1:
                if abs(int(tmp[0])) > res:
                    res = abs(int(tmp[0]))
            stack = tmp[::-1]
            tmp = []

    return res
