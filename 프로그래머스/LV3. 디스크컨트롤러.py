# 힙
# 진짜 ㅈㄴ어려웠음
# 뭔가 백준 보석도둑이랑 풀이가 비슷하다.
# 판단배열을 힙으로 만들고 그 중에서 최대나 최소를 골라서 작업하는 행위
# 즉 어떤 조건을 만족하는 원소들을 힙에 넣어주고 거기서 다시 판단하는 것임

import heapq


def solution(jobs):

    heap = []
    cnt = 0
    start = -1  # 바로 앞 job의 종료시각(첫 job의 경우는 -1)
    now = 0  # 현재 시점
    res = 0  # 답

    # 모든 job 처리할 때까지 -> heap에서 하나만 빼므로 아다리가 맞음
    while cnt < len(jobs):
        # 모든 job을 순회하며 해당 job이 현재 시점에서 처리할 수 있는지를 판단
        # job의 요청시각이 바로 앞 job의 종료시각과 현재시점 사이에 있어야한다.
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        # 현재 시점에서 처리할 수 있는 job이 하나 이상 있을 경우 그 중 최소 소요시간을 가진 job을 꺼낸다
        #
        if heap:
            curr = heapq.heappop(heap)
            # 바로 앞 job의 종료시각 업데이트
            start = now
            # 현재시각 += 방금꺼낸 job의 소요시간
            now += curr[0]
            cnt += 1
            # 대기시간 + 소요시간 = 현재시점 - 요청시점
            res += now - curr[1]
        else:
            now += 1

    return res//len(jobs)
