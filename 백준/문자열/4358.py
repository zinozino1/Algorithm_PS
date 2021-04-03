# 골드4-문자열-생태학
# 입력 개수가 없을 때는 공백을 기준으로 브레이크를 걸어준다.
# 그외에는 그냥 무난한 해시문제

import sys
input = sys.stdin.readline


def sol():

    # 딕셔너리사용
    dic = dict()

    while True:
        curr = input().strip()
        # 공백 입력 될때까지
        if curr == '':
            break
            # 중복 카운팅
        dic[curr] = dic.get(curr, 0) + 1

    tot = 0
    for v in dic.values():
        tot += v
    for v in dic.keys():
        dic[v] = round((dic.get(v) / tot * 100), 4)

    res = list(dic.items())
    res.sort(key=lambda x: (x[0]))

    # 소수점 (.0000)까지 출력해야함
    for x, y in res:
        print(x, '%.4f' % y)


sol()
