# 2512-실버3-이분탐색
# n = 10만이므로 완전탐색 불가능
# 전형적인 이분탐색 유형(갯수, 합)중에서 합 문제 -> 갯수문제는 capa 갯수 판단해야 하기 때문에 좀 더 어려움


import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():

    n = int(input())
    target = list(map(int, input().split()))
    total = int(input())

    lt = 1
    rt = max(target)

    def count(capa):
        tmp = []
        for x in target:
            if x >= capa:
                tmp.append(capa)
            else:
                tmp.append(x)
        return sum(tmp)

    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if count(mid) <= total:
            lt = mid + 1
            res = mid
        else:
            rt = mid - 1

    print(res)


sol()
