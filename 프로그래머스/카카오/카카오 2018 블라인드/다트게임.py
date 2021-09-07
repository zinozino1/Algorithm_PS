# 문자열 + 구현

def solution(dartResult):
    ans = 0
    scores = []
    curr = ''
    tmp = ''
    for dart in dartResult:
        if dart.isdigit():
            curr += dart
        elif dart.isalpha():
            if dart == "S":
                scores.append(int(curr))
            elif dart == "D":
                scores.append(int(curr) ** 2)
            elif dart == "T":
                scores.append(int(curr) ** 3)
            tmp += "a"
            curr = ""
        else:
            tmp += dart

    a_cnt = 0
    options = [''] * 3
    for i in range(len(tmp)):
        if tmp[i] == "a":
            a_cnt += 1
        else:
            if a_cnt == 1:
                options[0] = tmp[i]
            elif a_cnt == 2:
                options[1] = tmp[i]
            else:
                options[2] = tmp[i]

    for i in range(3):
        if options[i] == "*":
            if i == 0:
                scores[0] *= 2
            elif i == 1:
                scores[0] *= 2
                scores[1] *= 2
            elif i == 2:
                scores[1] *= 2
                scores[2] *= 2
        elif options[i] == "#":
            if i == 0:
                scores[0] = -scores[0]
            elif i == 1:
                scores[1] = -scores[1]
            elif i == 2:
                scores[2] = -scores[2]

    return sum(scores)
