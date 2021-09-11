# 재귀 + 문자열
# 재귀에 대한 이해가 더 필요


def is_correct_str(str):
    if len(str) == 0:
        return True
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)

    return True if len(stack) == 0 else False


def split(str):
    left_cnt = 0
    right_cnt = 0
    for s in str:
        if s == "(":
            left_cnt += 1
        elif s == ")":
            right_cnt += 1
        if left_cnt == right_cnt:
            break

    return str[:left_cnt+right_cnt], str[left_cnt+right_cnt:]


def recursive(str):
    if len(str) == 0:
        return ""
    u, v = split(str)
    if is_correct_str(u):
        return u + recursive(v)
    else:
        u = u[1:-1]
        tmp = ''
        for i in range(len(u)):
            if u[i] == ')':
                tmp += "("
            else:
                tmp += ")"
        return "("+recursive(v)+")"+tmp


def solution(p):
    if len(p) == 0:
        return ""
    res = recursive(p)
    return res
