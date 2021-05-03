def solution(s):

    curr = s
    curr = curr[1:len(curr)]
    curr = curr[:len(curr)-1]

    target = []
    flag = False
    comma_flag = False
    tmp = []
    tmp2 = ''
    for c in curr:
        if c == "{":
            flag = True
        elif c == "," and flag:
            tmp.append(tmp2)
            tmp2 = ''
        elif flag and c.isdigit():
            tmp2 += c
        elif c == "}":
            flag = False
            tmp.append(tmp2)
            target.append(tmp)
            tmp2 = ''
            tmp = []
    target.sort(key=len)

    res = [int(target[0][0])]
    prev = set(target[0])
    for i in range(1, len(target)):
        diff = set(target[i])-prev
        prev = set(target[i])
        res.append(int(list(diff)[0]))

    return res
