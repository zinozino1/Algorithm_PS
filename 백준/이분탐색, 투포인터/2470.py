# 이분탐색으로 어떻게 풀까 고민하다 결국 투포인터로 풀음
# 이분탐색 -> 정렬되어있어야함, logn 보장    투포인터 -> 정렬 안해도 됨, 최악의 경우 n
# 로직이 맞는데 계속 틀려서 뭔가 싶었더니 1e9로 설정했던 맥스값이 문제였음
# 이제부터 max 값은 sys.maxsize로 조지기


import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    target = list(map(int, input().split()))
    target.sort()

    lt = 0
    rt = n - 1
    minN = INF

    res = []

    while lt < rt:
        curr = target[lt] + target[rt]
        if abs(curr) < minN:
            minN = abs(curr)
            res = [target[lt], target[rt]]
        if curr >= 0:
            rt -= 1
        elif curr < 0:
            lt += 1

    print(*res)


sol()
