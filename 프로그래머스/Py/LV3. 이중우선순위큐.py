# 첫번째시도 max_heap, min_heap 두 개 사용해서 작업
# -> 맞긴 맞았으나 remove함수 때문에 n^2이다
# 생각해봤는데 식별자를 넣어줘도 n^2인 것 같음. 문제 자체가 이상하네

import heapq


def solution(operations):
    min_heap, max_heap = [], []

    for o in operations:
        curr = o.split()
        if curr[0] == "I":
            heapq.heappush(min_heap, int(curr[1]))
            heapq.heappush(max_heap, (-int(curr[1]), int(curr[1])))
        elif curr[0] == "D" and not max_heap or not min_heap:
            continue
        elif curr[0] == "D" and curr[1] == "1":
            item = heapq.heappop(max_heap)
            min_heap.remove(item[1])
        elif curr[0] == "D" and curr[1] == "-1":
            item = heapq.heappop(min_heap)
            max_heap.remove((-item, item))
    if max_heap and min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0, 0]
