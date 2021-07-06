# 골드4-텀프로젝트
# 그래프문제. 사이클 판단하기 2668과 거의 유사하다
# 이 문제에선 각 노드당 하나의 노드만 연결되지만 노드가 많아질것을 대비하여 인접리스트로 해봤음

import sys
sys.setrecursionlimit(111111)
T = int(input())


for _ in range(T):
    n = int(input())
    target = list(map(lambda x: x-1, list(map(int, input().split()))))
    adj = [[] for _ in range(n)]
    cycle = [0]*n
    for i in range(n):
        adj[i].append(target[i])

    visited = [0]*n
    res = 0

    def dfs(v):
        global res
        # 모든 연결 노드를 사이클에 무조건 넣음
        cycle.append(v)
        connected = adj[v]
        # dfs는 dfs안에서 visited업데이트 하자
        visited[v] = 1
        for c in range(len(connected)):
            # 방문하지 않은 곳이라면 이어서 재귀 탐색
            if visited[connected[c]] == 0:
                dfs(connected[c])
            # 방문한 곳이라면 사이클 정하기
            else:
                # 가고자하는 정점이 cycle 안에 있어야함
                if connected[c] in cycle:
                    # 사이클 끝점부터사이클 계산
                    res += len(cycle[cycle.index(connected[c]):])

    for i in range(n):
        if visited[i] == 0:
            # 하나의 탐색마다 하나의 사이클 만든다
            cycle = []
            dfs(i)

    print(n-res)
