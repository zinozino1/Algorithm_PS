# 기본 구현 및 해시 응용
# 풀이시간 35분정도

import sys
from collections import deque
input = sys.stdin.readline


def sol():

    t = int(input())
    cnt = 1
    for _ in range(t):
        dic = dict()

        n, k = map(int, input().split())
        target = input().rstrip()
        q = deque(list(target))

        for i in range(n//4):
            for j in range(4):
                dic[target[(n//4) * j: (n//4) * j + (n//4)]
                    ] = dic.get(target[(n//4) * j: (n//4) * j + (n//4)], 0) + 1
            tmp = q.pop()
            q.appendleft(tmp)
            target = "".join(list(q))

        res = [int(x, 16) for x in list(dic.keys())]
        res.sort(reverse=True)
        print("#%d %d" % (cnt, res[k-1]))
        cnt += 1


sol()
