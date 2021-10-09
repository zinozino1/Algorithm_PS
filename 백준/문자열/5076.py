# 골드4 - 웹페이지
# 문자열 + 스택

def sol():
    res = []
    while True:
        target = input().strip()
        if target == '#':
            break
        idx = 0
        stack = []
        while True:
            if idx >= len(target):
                break

            if target[idx] == "<":
                acc = ''
                while True:
                    if target[idx] == ">":
                        break
                    acc += target[idx]
                    idx += 1

                if acc[1:][len(acc)-2] == "/":
                    idx += 1
                    continue
                if acc[1:][0] == "/" and stack and stack[-1].split(" ")[0] == acc[2:]:
                    stack.pop()
                    idx += 1
                    continue
                elif acc[1:][0] == "/" and stack and stack[-1].split(" ")[0] != acc[2:]:
                    pass

                stack.append(acc[1:])

            idx += 1

        if stack:
            res.append("illegal")
        else:
            res.append("legal")

    return res


for s in sol():
    print(s)
