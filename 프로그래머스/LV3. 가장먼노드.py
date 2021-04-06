# 그래프 탐색

# 1. 인접행렬
# 노드개수 V, 간선개수 E
# adj_matrix[i][j]로 표현
# 연결여부확인 o(1), 탐색 o(V^2)
# 노드개수에 비해 간선 개수가 작다면 탐색효율 매우 떨어짐

# 2. 인접리스트
# 노드개수 V, 간선개수 E
# adj_list[i]에 연결된 노드 리스트 넣기(2차원 리스트)
# 연결여부확인 o(V), 탐색 o(V+E)
# 인접 행렬 탐색의 비효율성 극복 가능


from collections import deque


def solution(n, edge):

    q = deque()
    adj_list = [[] for _ in range(len(edge))]

    # 무향그래프 인접리스트 정의
    for i in range(len(edge)):
        start = edge[i][0]
        end = edge[i][1]
        adj_list[start].append(end)
        adj_list[end].append(start)

    visited = [0]*(n+1)
    visited[0] = 1
    visited[1] = 1
    q.append(1)
    res = 0
    while q:
        res = len(q)
        for _ in range(len(q)):
            curr_node = q.popleft()

            for i in range(len(adj_list[curr_node])):
                if visited[adj_list[curr_node][i]] == 0:
                    visited[adj_list[curr_node][i]] = 1
                    q.append(adj_list[curr_node][i])

    return res
