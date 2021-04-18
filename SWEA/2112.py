# copy.deepcopy()는 순수한 python 모듈이다. 거의 0.1초 이상을 잡아먹으니 [ layer[:] for layer in film ] 구문을 기억하자.
# 입력이 str이므로 str로 처리해야 하는 부분이 있다면 습관적으로 입력을 받을 때 map(int, ...)부분을 사용하지 말자.
# tuple이 list보다 빠르다.


import copy
from collections import deque


def sol():
    global min_cnt

    # 약품 처리 해야되는지 판단
    def is_success(arr):
        prev = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if cnt >= k:
                return 1
            if prev == arr[i]:
                cnt += 1
            else:
                prev = arr[i]
                cnt = 1
        if cnt >= k:
            return 1
        return 0

    # 약품 치는 모든 경우의 수
    def dfs(L, film, zero_tot, one_tot):
        global min_cnt

        # 가지치기
        if zero_tot > k or one_tot > k:
            return
        if zero_tot+one_tot >= min_cnt:
            return
        if L == d:
            res = 0
            for x in zip(*film):
                res += is_success(x)
            if res == w:
                if zero_tot+one_tot < min_cnt:
                    min_cnt = zero_tot+one_tot

            return

        else:
            tmp_film = [layer[:] for layer in film]

            # 안 바뀌는 경우
            dfs(L + 1, tmp_film, zero_tot, one_tot)

            # 행이 0으로 바뀜
            tmp_film[L] = [0]*w
            dfs(L+1, tmp_film, zero_tot+1, one_tot)
            tmp_film[L] = tmp_film[L][::]

            # 행이 1로 바뀜
            tmp_film[L] = [1]*w
            dfs(L+1, tmp_film, zero_tot, one_tot+1)
            tmp_film[L] = tmp_film[L][::]

    t = int(input())

    for test_case in range(1, t+1):
        d, w, k = map(int, input().split())

        film = [tuple(map(int, input().split())) for _ in range(d)]

        min_cnt = 1e9
        success_cnt = 0
        for arr in zip(*film):
            success_cnt += is_success(arr)

        # 약품 처리 안하고 바로 통과
        if success_cnt == w:
            min_cnt = 0
        # 약품 처리 해야함
        elif k == 1:
            min_cnt = 0
        else:
            dfs(0, film, 0, 0)

        print("#%d %d" % (test_case, min_cnt))


sol()
