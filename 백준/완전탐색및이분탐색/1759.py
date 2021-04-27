# 골드5-암호 만들기-완전탐색

import itertools as it


def sol():

    # 모음
    m = ['a', 'e', 'i', 'o', 'u']

    L, C = map(int, input().split())
    target = list(input().strip().split())
    res = []
    # lCr 하고 뽑은 원소 정렬
    for tmp in it.combinations(target, L):
        s = list(tmp)
        s.sort()
        res.append(s)
    # 다시 정렬
    res.sort()
    for r in res:
        j_cnt = 0  # 자음 카운트
        m_cnt = 0  # 모음 카운트
        for i in range(L):
            if r[i] in m:
                m_cnt += 1
            else:
                j_cnt += 1
        if j_cnt < 2 and m_cnt < 1:
            continue
        elif j_cnt > 1 and m_cnt > 0:
            print("".join(r))


sol()
