import heapq
from collections import deque
import sys
input = sys.stdin.readline


def sol():

    n = int(input())

    target = [input().strip() for _ in range(n)]

    dic = dict()

    for i in range(n):
        for j in range(len(target[i])):
            # 우선순위 딕셔너리에 정의 -> 자리수 기준으로 누적합 계산
            dic[target[i][j]] = dic.get(
                target[i][j], 0) + 10**(len(target[i])-j-1)

    # 딕셔너리 정렬(내림차순)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    cnt = 9
    for tu in dic:
        ch = tu[0]
        # 문자열 숫자로 치환
        for i in range(n):
            for j in range(len(target[i])):
                if target[i][j] == ch:
                    target[i] = target[i].replace(ch, str(cnt))

        cnt -= 1
    res = 0
    for x in target:
        res += int(x)
    print(res)


sol()
