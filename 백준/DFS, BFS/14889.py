# 실버3-스타트와링크
import copy
from collections import deque
import itertools as it

# 15:14-15:45


def sol():

    global min_diff

    def dfs(L, s, res):
        global min_diff
        if L == n//2:
            start = list(map(int, res))
            link = list(set(list(range(1, n+1)))-set(start))

            start_score = 0
            link_score = 0
            for i in range(n//2-1):
                for j in range(i+1, n//2):

                    start_score += score[start[i]-1][start[j]-1] + \
                        score[start[j]-1][start[i]-1]
                    link_score += score[link[i]-1][link[j]-1] + \
                        score[link[j]-1][link[i]-1]

            if abs(start_score - link_score) < min_diff:
                min_diff = abs(start_score - link_score)

            return
        else:
            for i in range(s, n):
                dfs(L+1, i+1, res+str(i+1))

    min_diff = 1e9
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]

    dfs(0, 0, '')

    print(min_diff)


sol()
