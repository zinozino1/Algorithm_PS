# 실버1-그리디-신입사원
# 튜플원소 하나 기준으로 정렬하고 smallest or largest 계속 갱신해주면 o(n)으로 풀이 가능


import heapq
import sys
input = sys.stdin.readline


def sol():

    t = int(input())

    for _ in range(t):
        n = int(input())

        target = [tuple(map(int, input().split())) for _ in range(n)]
        # 서류성적순위 기준 정렬
        target.sort()

        smallest = 1e9
        cnt = 0

        # 순차 탐색 -> smallest 갱신
        for p in target:
            if p[1] < smallest:
                smallest = p[1]
                cnt += 1

        print(cnt)


sol()
