class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)
        for i in range(n):
            for j in range(m):
                if (i in (0, n-1) or j in (0, m-1)) and grid[i][j] == 0:
                    dfs(i, j)
        c = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    c += 1
        return c