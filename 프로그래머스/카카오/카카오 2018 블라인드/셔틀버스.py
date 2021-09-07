# timetable sorting 안되어있음

# 문제 설명과 다르게 24: 00 등 datetime 을 쓰면 문제가 될 요소가 존재하므로 60*h+m 으로 변형해서 문제 해결후 다시 형변환을 하는걸 추천

# 콘은 무조건 마지막 버스에 타야함. 어떤 조건이든 마지막 버스보다 일찍 타면 틀린 알고리즘

# 마지막버스에 자리가 있으면 남은 인원과 관계없이 마지막버스 시간에만 도착하면 됨

# 마지막버스에 자리가 없으면 남은 인원중 가장 "먼저"가 아닌 가장"마지막에" 도착한 한명보다만 빨리 도착하면됨.


import heapq


def solution(n, t, m, timetable):
    curr_bus = 540
    timetable = [int(time.split(":")[0]) * 60 + int(time.split(":")[1])
                 for time in timetable]
    timetable.sort()
    res = 0

    for i in range(n, 0, -1):

        if i > 1:  # 마지막 이전의 버스들
            passenger_cnt = 0
            will_delete = []
            for idx, p_time in enumerate(timetable):
                if p_time <= curr_bus and passenger_cnt < m:
                    will_delete.append(p_time)
                    passenger_cnt += 1
            for will in will_delete:
                timetable.remove(will)

        elif i == 1:  # 마지막 버스에 타야함
            for idx, p_time in enumerate(timetable):
                heap = []
                passenger_cnt = 0
                for p_time in timetable:
                    if p_time <= curr_bus:
                        passenger_cnt += 1
                        heapq.heappush(heap, p_time)

                # 자리 있음
                if passenger_cnt < m:
                    res = curr_bus
                    break
                # 자리 없음
                else:
                    for _ in range(m):
                        nxt = heapq.heappop(heap)
                        res = nxt - 1

        # 버스 업데이트
        curr_bus += t

    ans = ''
    if res // 60 < 10:
        ans += "0"+str(res//60)
    else:
        ans += str(res//60)
    ans += ":"
    if res % 60 < 10:
        ans += "0"+str(res % 60)
    else:
        ans += str(res % 60)

    return ans
