# 실버2 - 괄호의 값
# 스택

# 예외처리 드럽게 많음 + 코드 더러움
# 다른 사람 코드도 더럽네 ㅋㅋ


target = list(input().strip())
stack = []


def sol():
    for t in target:
        if t == ")":
            num = 0
            while stack and stack[-1] != "(":
                curr = stack.pop()
                if not curr.isalnum():
                    print(0)
                    return
                num += int(curr)
            if not stack:
                print(0)
                return
            stack.pop()
            if num == 0:
                stack.append("2")
            else:
                stack.append(str(2*num))
        elif t == "]":
            num = 0
            while stack and stack[-1] != "[":
                curr = stack.pop()
                if not curr.isalnum():
                    print(0)
                    return
                num += int(curr)
            if not stack:
                print(0)
                return
            stack.pop()
            if num == 0:
                stack.append("3")
            else:
                stack.append(str(3 * num))
        else:
            stack.append(t)

    if any(not s.isalnum() for s in stack):
        print(0)
        return
    res = 0
    for s in stack:
        res += int(s)
    print(res)


sol()

