# 힙
# 예외처리 잘해야한다..

import heapq as hq
import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    success_flag = False
    while scoville:

        if all(x >= K for x in scoville):
          # 필요없는 작업임 -> 스코빌지수를 모두 체크하는 것이 아니라 가장 작은 것만 K를 넘는지만 체크해야함
            success_flag = True
            break
        if len(scoville) == 1:
            if scoville[0] >= K:
                success_flag = True
            break

        cnt += 1
        if len(scoville) > 1:
            lowest = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, lowest + second * 2)

    # 이것도 비효율적..
    if not success_flag:
        return -1
    else:
        return cnt


# 다른 사람 풀이


def solution2(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:  # 가장작은것이 K를 넘으면 모든 원소가 K를 넘는다.
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer
