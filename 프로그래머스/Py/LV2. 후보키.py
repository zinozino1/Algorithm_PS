# 완전탐색 + 문자열 + 해시

from itertools import combinations
from collections import deque
import itertools as it


def solution(relation):

    combi_dic = {}
    zip_arr = []

    # 전치행렬로 변경 + 전치행렬 맨 앞에 식별자 넣기
    for i, tmp in enumerate(zip(*relation)):
        inserted_arr = list(tmp)
        inserted_arr.insert(0, "att"+str(i))
        zip_arr.append(inserted_arr)

    # 속성 뽑는 경우의 수 구하기
    for i in range(1, len(relation)+1):
        for tmp in it.combinations(zip_arr, i):

            init_combi = ''
            s = set()
            dic_exist_flag = False
            # 속성 쌍 판별하기 위해 loop돌림 -> loop 거꾸로 돌기 주의
            for k in range(len(tmp[0])):
                joo = []
                for l in range(len(tmp)):
                    joo.append(tmp[l][k])
                # 속성에서 식별자 값으로 최소성 판단 -> 딕셔너리에 이미 있을 경우 최소성 만족 x
                if k == 0:
                    init_combi = " ".join(joo)
                    for a in range(len(joo)+1):
                        for q in it.combinations(joo, a):
                            tmp_list = list(q)
                            tmp_list.sort()

                            # -> combi_dic[" ".join(tmp_list)]으로 하면 에러남
                            if combi_dic.get(" ".join(tmp_list)):
                                dic_exist_flag = True

                s.add(tuple(joo))
            # 뽑은 속성 조합이 딕셔너리에 없고(최소성), 키의 조건을 만족한다면(유일성)
            if not dic_exist_flag and len(s) == len(tmp[0]):
                combi_dic[init_combi] = 1

    return len(combi_dic.keys())


# 고수 풀이


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]  # 중요
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)
