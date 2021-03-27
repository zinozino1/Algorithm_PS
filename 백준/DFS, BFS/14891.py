# 골드5-톱니바퀴
# 시뮬레이션 -> 재귀이용 풀이
# 문제 잘못이해해서 헛짓거리했음
# 오른쪽, 왼쪽 연쇄적으로 확인해야하므로 재귀를 사용해야한다
# 주의점 1) 돌리기전에 인접 톱니가 돌아갈 수 있는지 확인해야함
# 주의점 2) 오른쪽판단은 인덱스 2와 6의 비교, 왼쪽판단은 인덱스 6과 2의 비교임
# 덱을 이용하면 좀 더 깔끔하게 로테이트할 수 있었음

import sys
from collections import deque

input = sys.stdin.readline


def sol():
    target = [list(map(int, input().strip())) for _ in range(4)]
    order_cnt = int(input())
    orders = []
    for _ in range(order_cnt):
        target_num, dir = map(int, input().split())
        orders.append((target_num, dir))

    def left_side(curr, next, dir):
        if next == -1:
            return
        else:
            if target[curr][6] != target[next][2]:
                left_side(curr - 1, next - 1, -dir)
                if dir == -1:
                    item = target[next].pop(0)
                    target[next].append(item)
                else:
                    item = target[next].pop()
                    target[next].insert(0, item)
            else:
                return

    def right_side(curr, next, dir):
        if next == 4:
            return
        else:
            if target[curr][2] != target[next][6]:
                right_side(curr + 1, next + 1, -dir)
                if dir == -1:
                    item = target[next].pop(0)
                    target[next].append(item)
                else:
                    item = target[next].pop()
                    target[next].insert(0, item)
            else:
                return

    for order in orders:
        target_num = order[0]
        dir = order[1]
        left_side(target_num - 1, target_num - 2, -dir)
        right_side(target_num - 1, target_num, -dir)
        if dir == -1:
            item = target[target_num - 1].pop(0)
            target[target_num - 1].append(item)
        else:
            item = target[target_num - 1].pop()
            target[target_num - 1].insert(0, item)

    res = 0
    for i in range(4):
        if target[i][0] == 1:
            res += pow(2, i)
    print(res)


sol()
