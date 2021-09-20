# dfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def dfs(x, y):
            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == "1":
                    check[nx][ny] = 1
                    dfs(nx, ny)

        check = [[0]*m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and check[i][j] == 0:
                    check[i][j] = 1
                    dfs(i, j)
                    cnt += 1

        return cnt
