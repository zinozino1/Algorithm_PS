# 해시
# dic.get(x, 0) + 1 => 아주 중요한 테크닉


import sys
input = sys.stdin.readline


def solution(participant, completion):

    dic = dict()
    answer = ''
    for x in participant:
        dic[x] = dic.get(x, 0)+1
    for x in completion:
        dic[x] = dic.get(x, 0)-1

    for p in dic.keys():
        if dic[p] == 1:
            answer = p

    return answer
