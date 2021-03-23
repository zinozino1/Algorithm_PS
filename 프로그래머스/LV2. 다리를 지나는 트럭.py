# 큐
# 변수가 많아서 헷갈릴 수 있음
# truck_weights는 이미 배열이므로 새로 큐를 생성할 필요 없었음

import sys
from collections import deque


def solution(bridge_length, weight, truck_weights):

    q = deque(truck_weights)
    bridge = deque([0]*(bridge_length + 1))

    tot_time = 0
    w_sum = 0
    bridge_cnt = 0

    while True:
        bridge.append(bridge.popleft())

        if bridge[0] != 0:
            w_sum -= bridge[0]
            bridge[0] = 0
            bridge_cnt -= 1

        if q and q[0] + w_sum <= weight:
            truck = q.popleft()
            w_sum += truck
            bridge[-1] = truck
            bridge_cnt += 1

        tot_time += 1

        if bridge_cnt == 0:
            break

    return tot_time
