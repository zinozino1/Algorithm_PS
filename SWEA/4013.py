import copy
from collections import deque


def sol():

    t = int(input())

    for test_case in range(1, t+1):
        order_cnt = int(input())
        target = [list(map(int, input().split())) for _ in range(4)]
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
        print("#%d %d" % (test_case, res))



sol()
