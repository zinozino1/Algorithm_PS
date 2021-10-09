# 골드4 - 무한수열
# dp

# top-down dp
# key값이 없으면 defaultdict값은 무조건  0 (int 일경우)

from collections import defaultdict
n, p, q = map(int, input().split())

dic = defaultdict(int)
dic[0] = 1


def recur(N):
    if dic[N] != 0:
        return dic[N]
    else:
        dic[N] = recur(N//p)+recur(N//q)
        return dic[N]


print(recur(n))
