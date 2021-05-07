def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    tmp = ''
    for n in new_id:
        if n.isalpha() or n.isdigit() or n == "-" or n == "_" or n == ".":
            tmp += n

    # 3단계
    stack = list(tmp)[::-1]
    tmp = []
    while stack:
        curr = stack.pop()
        if curr == ".":
            if stack and stack[-1] == ".":
                stack.pop()
                stack.append(curr)
            else:
                tmp.append(curr)
        else:
            tmp.append(curr)

    # 4단계
    if tmp[0] == "." and tmp[-1] != ".":
        tmp = tmp[1:len(tmp)]
    elif tmp[-1] == "." and tmp[0] != ".":
        tmp = tmp[:len(tmp)-1]
    elif tmp[0] == "." and tmp[-1] == ".":
        tmp = tmp[1:len(tmp)-1]

    # 5단계
    if not tmp:
        tmp = ["a"]

    # 6단계
    if len(tmp) > 15:
        tmp = tmp[:15]
        if tmp[-1] == ".":
            tmp = tmp[:len(tmp)-1]

    # 7단계
    res = tmp[:]
    if len(tmp) < 3:
        while True:
            if len(res) == 3:
                break
            res.append(tmp[-1])
    res = "".join(res)
    return res
