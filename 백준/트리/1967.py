# 골드4 - 트리의 지름
# 트리

# 문제 조건상 트리를 그래프 형태로 구현함 -> 부모 자식 관계가 없으므로
# 노드의 모든 끝점에서 끝점 거리를 계산 했더니 TLE
# 아무 정점이나 하나 잡고 가장 긴 거리를 가진 노드를 찾으면 그것이 트리의 지름 정점중 하나
# 그 노드부터 다시 가장 긴 거리를 갖는 노드를 찾으면 된다.

# 트리의 지름 공식인듯

import sys
sys.setrecursionlimit(100000)
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, v = map(int, input().split())
    tree[s].append((e, v))
    tree[e].append((s, v))

next_node = -1
maxN = -1e9
res = -1e9


def dfs(v, tot, flag):
    global maxN, next_node, res
    visited[v] = 1
    for ne in tree[v]:
        # 끝점을 파악하는 방법
        if visited[ne[0]] == 1 and len(tree[v]) == 1:
            if tot > maxN:
                maxN = tot
                next_node = v
            if flag and tot > res:
                res = tot
        if visited[ne[0]] == 0:
            dfs(ne[0], tot+ne[1], flag)


visited = [0] * (n + 1)
dfs(1, 0, False)
visited = [0] * (n + 1)
dfs(next_node, 0, True)
if n == 1:
    print(0)
else:
    print(res)
