# 실버2 - 트리의 부모 찾기
# 트리

# 문제 조건상 트리를 그래프 형태로 구현해야함 -> 부모 자식 관계가 없으므로
# dfs로 들어가기 전에 검사를 하는데 이 때 검사할 노드의 부모가 설정되지 않았다면 현재 노드가 부모가 된다.

import sys
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n+1)]
check = [0]*(n+1)

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
parents = [0]*(n+1)


def traverse(v):
    for ne in tree[v]:
        if parents[ne] == 0:
            parents[ne] = v
            traverse(ne)


traverse(1)
for i in range(2, n+1):
    print(parents[i])
