# 완전탐색
# 그래프탐색임 격자탐색만 풀어보다가 인접행렬 활용한 거 푸니까 헷갈렸음.. 단순 dx,dy만 고려하지 말자
# 연쇄적으로 탐색하는 것을 재귀로 구현

def solution(n, computers):

    def dfs(com):
        visited[com] = 1
        # 해당 노드가 다른 노드들과 연결되어있는지 반복문을 통해 확인
        for j in range(n):
            if com == j:
                continue
            # 연결되어 있다면 연쇄탐색 시작
            if visited[j] == 0 and computers[com][j] == 1:
                dfs(j)

    visited = [0] * n
    res = 0
    for i in range(n):
        if visited[i] == 0:
            res += 1
            dfs(i)
            # dfs완료되면 한개의 연쇄적 네트워크 완성

    return res
