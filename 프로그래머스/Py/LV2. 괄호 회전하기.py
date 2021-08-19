# 무난한 문자열 + 스택 문제

def check_correct(str):
    stack = []
    for s in str:
        if s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
        elif s == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    if not stack:
        return True
    else:
        return False


def rotate(str):
    res = ''
    cnt = 0
    for i in range(len(str)-1):
        tmp = str[i:]+str[:i]
        if check_correct(tmp):
            cnt += 1
    return cnt


def solution(s):
    return rotate(s)
