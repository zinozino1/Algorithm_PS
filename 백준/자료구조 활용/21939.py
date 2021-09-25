# 골드4 - 문제추천시스템 ver.1
# 우선순위 큐


# 이중우선순위큐 사용해야함 -> 동기화를 위해 마킹을 해준다
# 이미 푼 문제와 같은 번호가 들어왔을 때 주의

import heapq

n = int(input())
problems = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())

solved = [0]*100001
max_heap = []
min_heap = []
for problem in problems:
    heapq.heappush(min_heap, (problem[1], problem[0]))
    heapq.heappush(max_heap, (-problem[1], -problem[0]))

for _ in range(m):
    order = list(input().split())
    if order[0] == "add":
        num, level = order[1], order[2]
        heapq.heappush(min_heap, (int(level), int(num)))
        heapq.heappush(max_heap, (-int(level), -int(num)))

    elif order[0] == "recommend":
        if order[1] == "-1":
            while min_heap:
                if solved[min_heap[0][1]] == 1 or solved[min_heap[0][1]] == min_heap[0][0]:
                    solved[min_heap[0][1]] = min_heap[0][0]
                    heapq.heappop(min_heap)
                else:
                    break
            print(min_heap[0][1])
        elif order[1] == "1":
            while max_heap:
                if solved[-max_heap[0][1]] == 1 or solved[-max_heap[0][1]] == -max_heap[0][0]:
                    solved[-max_heap[0][1]] = -max_heap[0][0]
                    heapq.heappop(max_heap)
                else:
                    break
            print(-max_heap[0][1])

    elif order[0] == "solved":
        solved[int(order[1])] = 1
