# 골드5 - 게리멘더링
# 그래프 dfs


import itertools as it

n = int(input())
tmp = list(map(int, input().split()))

info = []
for i, v in enumerate(tmp):
    info.append((i+1, v))

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    target = list(map(int, input().split()))
    for j in range(1, target[0]+1):
        graph[i].append((target[j], info[target[j]-1][1]))


def dfs(node, op):
    check[node] = 1

    for next in graph[node]:
        if op == 1:
            if check[next[0]] == 0 and next in first:
                dfs(next[0], 1)
        else:
            if check[next[0]] == 0 and next in second:
                dfs(next[0], 2)


minScore = 1e9
for i in range(1, n):
    for tmp in it.combinations(info, i):

        first = list(set(tmp))
        second = list(set(info)-set(tmp))

        first_flag = False
        second_flag = False

        check = [0]*(n+1)
        dfs(first[0][0], 1)
        if sum(v == 1 for v in check) == len(first):
            first_flag = True

        check = [0]*(n+1)
        dfs(second[0][0], 2)
        if sum(v == 1 for v in check) == len(second):
            second_flag = True

        if first_flag and second_flag:
            first_sum = sum(v[1] for v in first)
            second_sum = sum(v[1] for v in second)
            minScore = min(minScore, abs(first_sum-second_sum))

if minScore == 1e9:
    print(-1)
else:
    print(minScore)
