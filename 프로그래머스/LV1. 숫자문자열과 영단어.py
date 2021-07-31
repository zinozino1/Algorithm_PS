# 문자열과 replace

def solution(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    while True:
        if s.isdecimal():
            break
        for k in dic.keys():
            if k in s:
                s = s.replace(k, str(dic[k]))
    return int(s)
