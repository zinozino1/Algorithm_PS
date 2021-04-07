# 골드4-그리디-카드정렬하기

import heapq
import sys
input = sys.stdin.readline


def sol():

    n = int(input())
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(input()))

    res = 0
    while len(heap) > 1:
        v1 = heapq.heappop(heap)
        v2 = heapq.heappop(heap)
        res += v1+v2
        heapq.heappush(heap, v1+v2)

    print(res)


sol()
