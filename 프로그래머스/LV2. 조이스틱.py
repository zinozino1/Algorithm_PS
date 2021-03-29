# 그리디
# 좌우) 현재 위치(ptr)에서 왼,오른방향의 "A"가 아닌 문자를 찾고 거리가 가장 짧은 곳으로 ptr 이동
# 상하) 일단 tmp배열을 상하 min 값으로 초기화
# 주의점 : while 조건식에 배열 음수값 들어가면 안되는듯 -> True로 하고 밑에 조건문으로 넣어야함


def solution(name):

    ptr = 0

    tmp = []
    for i in range(len(name)):
        tmp.append(min(ord(name[i])-ord("A"), ord("Z")-ord(name[i])+1))
    res = sum(tmp)
    tmp[ptr] = 0
    while True:
        if all(x == 0 for x in tmp):
            break

        lt = ptr-1
        rt = ptr+1
        lt_cnt = 1
        rt_cnt = 1

        while True:
            if tmp[lt] != 0:
                break
            lt_cnt += 1
            lt -= 1
        while True:
            if tmp[rt] != 0:
                break
            rt_cnt += 1
            rt += 1
        if lt_cnt >= rt_cnt:
            ptr = rt
            res += rt_cnt
        else:
            ptr = lt
            res += lt_cnt
        tmp[ptr] = 0

    return res
