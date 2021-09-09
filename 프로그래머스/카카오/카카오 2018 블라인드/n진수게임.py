# 진법 + 문자열
# 35분

def convert(num, b):
    if num == 0:
        return "0"
    dic = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    res = ''
    while num >= 1:
        if dic.get(str(num % b)):
            res += dic[str(num % b)]
        else:
            res += str(num % b)
        num //= b
    return res[::-1]


def solution(n, t, m, p):

    tmp = ''
    for i in range(t*m):
        tmp += convert(i, n)

    res = ''
    for i in range(p-1, t*m, m):
        if t == len(res):
            break
        res += tmp[i]

    return res
