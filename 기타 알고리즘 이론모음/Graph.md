```py

1. 인접행렬
# 노드개수 V, 간선개수 E
# adj_matrix[i][j]로 표현
# 연결여부확인 o(1), 탐색 o(V^2)
# 노드개수에 비해 간선 개수가 작다면 탐색효율 매우 떨어짐

2. 인접리스트 *****
# 노드개수 V, 간선개수 E
# adj_list[i]에 연결된 노드 리스트 넣기(2차원 리스트)
# 연결여부확인 o(V), 탐색 o(V+E)
# 인접 행렬 탐색의 비효율성 극복 가능


* 인접리스트 활용 그래프 생성법

n,m = map(int,input().split())
  grid = [[] for _ in range(m)]
  # 인접 리스트 정의
  for _ in range(m):
    x,y,w = map(int,input().split())
    grid[x].append((y,w))
    grid[y].append((x,w))



* 인접리스트 활용 DFS 탐색
-> 경로 경우의 수 찾기

1) 시작노드와 끝노드가 정해져있을 때

  def dfs(v):
    visited[v] = 1
    if v == end:
      print("끝점 도착 ")
      return

    # 현재 노드와 연결된 노드 반복문으로 탐색 -> 모든 노드를 검색하는 것이 아닌 연결된 노드만 검색하는 것
    for s in grid[v]:
      if visited[s[0]] == 0:
        dfs(s[0])
        visited[s[0]] = 0

2) 시작노드만 정해져있을 때 -> 경우의 수 아니고 모든 노드 순회

  def dfs(v):
    visited[v] = 1
    if v == end:
      print("끝점 도착 ")
      return

    # 현재 노드와 연결된 노드 반복문으로 탐색
    for s in grid[v]:
      if visited[s[0]] == 0:
        dfs(s[0])
        -> 이친구만 없애주면 된다 이것이 백트래킹이기 때문
        # visited[s[0]] = 0


* 인접리스트 활용 BFS 탐색
-> 최단 경로 찾기 맞나?

1) 시작노드만 정해져있을 때

  def bfs():
    visited = [0]*m

    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
      for _ in range(len(q)):
        curr = q.popleft()
        print(curr)

        for s in grid[curr]:
          if visited[s[0]] == 0:
            visited[s[0]] = 1
            q.append(s[0])





```
