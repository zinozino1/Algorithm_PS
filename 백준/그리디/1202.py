# 골드2-그리디-보석도둑
# 보석 기준으로 가방에 넣으려다 시간초과로 실패
# 가방 기준으로 푸니 성공


import heapq
from collections import deque
import sys
input = sys.stdin.readline


def sol():
    N, K = map(int, sys.stdin.readline().split())
    # 보석을 가장 낮은 무게가 맨 위로 가도록 힙 정의
    j = []
    for _ in range(N):
        heapq.heappush(j, list(map(int, sys.stdin.readline().split())))
    b = []
    # 낮은 무게 순으로 가방 정렬
    for _ in range(K):
        b.append(int(sys.stdin.readline()))
    b.sort()

    res = 0
    tmp_jew = []  # heap
    # 가방을 기준으로 찾는다.
    for x in b:
        # 가방의 무게를 만족하는 보석들을 힙에 넣기 -> o(1)
        while j and x >= j[0][0]:
            # 보석의 가치 기준으로 힙에 넣어줌
            heapq.heappush(tmp_jew, -heapq.heappop(j)[1])
        # 만족하는 보석이 있음
        if tmp_jew:
            # 만족하는 보석 중 가장 가치가 높은 보석 답에 더해줌
            res -= heapq.heappop(tmp_jew)
        # 가방을 무게순으로 오름차순 정렬했기 때문에 만족하는 보석이 없는 경우는 바로 브레이크
        elif not j:
            break
    print(res)


sol()
