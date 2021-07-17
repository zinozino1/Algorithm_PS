# 실버1 - 맥주마시면서 걸어가기
# BFS

# 머리가 안돌아가서 빡친 문제
# 왜 BFS인가? -> 도착지에 '도달'할 수 있기만 하면 된다. 도달 즉시 브레이크를
# 걸어야해서 최단거리에 적합한 BFS가 더 낫다

from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    convi = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))

    q = deque()
    q.append(start)
    check = set()
    check.add(tuple(start))
    flag = False
    while q:
        for _ in range(len(q)):
            pos = q.popleft()
            x, y = pos[0], pos[1]

            # 현재 좌표가 목적지에 도달할 수 있는 좌표면 브레이크
            if abs(end[0]-x)+abs(end[1]-y) <= 1000:
                flag = True
                q = []
                break

            # 다음 좌표가 현재 좌표에서 도달할 수 있는 좌표면 큐에 넣기
            for next in convi:
                if tuple(next) in check:
                    continue
                nx, ny = next[0], next[1]
                if abs(nx-x)+abs(ny-y) <= 1000:
                    q.append(next)
                    check.add(tuple(next))

    if flag:
        print("happy")
    else:
        print("sad")
