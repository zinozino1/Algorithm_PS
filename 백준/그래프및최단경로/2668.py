# 골드5-숫자고르기-그래프 및 DFS
# 완전탐색 DFS로 풀다가 n=100인 것을 보고 그래프 cycle로 풀이 변경
# 사이클 노드를 확인하면 된다
# 무조건 다시 풀어보기..

n = int(input())
target = [int(input()) for _ in range(n)]
# 전체 경로에서 방문했는지 체크
visited = [0]*n
cycle = [0]*n
# 인접리스트 정의 -> 유향그래프로 그래야 사이클 판단 가능
adj = [[] for _ in range(n)]
for i in range(n):
    adj[i].append(target[i]-1)


def dfs(v):
    visited[v] = 1
    tmp_visited[v] = 1

    connected = adj[v]
    for s in range(len(connected)):
        # 방문되지 않은 곳이면 재귀 순회
        if tmp_visited[connected[s]] == 0:
            dfs(connected[s])
        # 이미 방문된 곳이면 -> cycle을 만족하는지 판단해야함
        else:
            # 다음 노드가 이미 cycle이라면 그냥 리턴
            if cycle[connected[s]] == 1:
                return
            # 시작점과 사이클의 끝점이 일치하지 않는다면 visited 초기화 후 리턴
            if start.index(1) != connected[s]:
                for idx, val in enumerate(tmp_visited):
                    if val == 1:
                        visited[idx] = 0
                return
            # 길이가 1짜리 싸이클이라면
            if len(tmp_visited) == 1:
                cycle[v] = 1
                return
            # 시작점과 끝점이 동일하면 tmp_visited에 방문한 경로를 순회하여 사이클 생성
            for idx, val in enumerate(tmp_visited):
                if val == 1:
                    cycle[idx] = 1
            return


for i in range(n):
    if visited[i] == 0:  # 전역 visited는 여기서 밖에 안씀
        # 노드 순회할때마다 tmp임시 배열 생성 -> cycle 판단하기 위해
        tmp_visited = [0]*n
        # 시작점 정의
        start = [0]*n
        start[i] = 1
        dfs(i)
print(cycle.count(1))
for i, c in enumerate(cycle):
    if c == 1:
        print(i+1)

# 9466 풀고 다시 푼 것

n = int(input())
target = [int(input()) for _ in range(n)]
visited = [0]*n
cycle_cnt = 0
cycle_set = set()

adj = [[] for _ in range(n)]
for i in range(n):
    adj[i].append(target[i]-1)


def dfs(v):
    global cycle_cnt
    visited[v] = 1
    connected = adj[v]
    cycle.append(v)
    for s in range(len(connected)):
        if visited[connected[s]] == 0:
            dfs(connected[s])
        else:
            if connected[s] in cycle:
                cycle_cnt += len(cycle[cycle.index(connected[s]):])
                for c in cycle[cycle.index(connected[s]):]:
                    cycle_set.add(c+1)


for i in range(n):
    if visited[i] == 0:
        cycle = []
        dfs(i)

print(cycle_cnt)
for s in sorted(list(cycle_set)):
    print(s)
