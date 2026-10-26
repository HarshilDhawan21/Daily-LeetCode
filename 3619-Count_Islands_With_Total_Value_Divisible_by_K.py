class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        c = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            s = grid[i][j]
            grid[i][j] = 0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                s += dfs(i + di, j + dj)
            return s
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        c += 1
        return c     