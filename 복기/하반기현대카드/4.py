# 4번 도로깔기
# 투포인터


# 못풀음
# 투포인터로 풀 수 있는 것 같은데 코드가 난해하다 다시 풀이 필요


def getMax(str, n):
    zero = []
    for i in range(len(str)):
        if str[i] == "0":
            zero.append(i)

    level = 0
    lt = zero[level]
    rt = zero[level+n-1]
    res = -1e9
    while True:
        if lt == 0:
            plt = lt
            prt = rt
            tmp = 0
            while plt <= prt:
                tmp += int(str[plt])
                plt += 1
            res = max(res, int(str[rt+1])+tmp)
        elif rt == len(str)-1:
            plt = lt
            prt = rt
            tmp = 0
            while plt <= prt:
                tmp += int(str[plt])
                plt += 1
            res = max(res, int(str[lt-1])+tmp)
        else:
            plt = lt
            prt = rt
            tmp = 0
            while plt <= prt:
                tmp += int(str[plt])
                plt += 1
            res = max(res, int(str[lt-1])+int(str[rt+1])+n+tmp)

        level += 1
        if level + n - 1 >= len(zero):
            break
        lt = zero[level]
        rt = zero[level + n - 1]

    return res


def solution(road, n):
    cnt = 0
    tmp = ''
    for r in road:
        if r == "1":
            cnt += 1
        elif r == "0":
            if cnt != 0:
                tmp += str(cnt)
            tmp += "0"
            cnt = 0
    tmp += str(cnt)

    if road.count("0") <= n:
        return len(road)
    else:
        return getMax(tmp, n)


print(solution("111011110011111011111100011111", 3))
print(solution("00001100011000000001", 3))
print(solution("001100", 5))
