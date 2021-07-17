# 실버2-부분수열의 합
# DFS

# 라이브러리 이용 풀이
import itertools as it

n, s = map(int, input().split())

target = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    for tmp in it.combinations(target, i):
        if sum(tmp) == s:
            cnt += 1

print(cnt)

# 재귀 풀이 -> 헛짓거리함
# 부분집합은 조합의 상위버전이다.

n, s = map(int, input().split())

target = list(map(int, input().split()))
cnt = 0


def dfs(L, tot):
    global cnt
    if L == n:
        if tot == s:
            cnt += 1
        return
    else:
        dfs(L+1, tot+target[L])
        dfs(L+1, tot)


dfs(0, 0)
if s == 0:
    print(cnt-1)
else:
    print(cnt)
