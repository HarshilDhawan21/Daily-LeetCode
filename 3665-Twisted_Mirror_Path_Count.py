class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        modulo = 10**9 + 7
        m, n = len(grid), len(grid[0])
        the_list = [[[0, 0] for _ in range(n)] for _ in range(m)]
        the_list[0][0][0] = 1
        for i in range(m):
            for j in range(n):
                r, d = the_list[i][j]
                if grid[i][j] == 0:
                    total = (r + d) % modulo
                    if j + 1 < n:
                        the_list[i][j + 1][0] = (the_list[i][j + 1][0] + total) % modulo
                    if i + 1 < m:
                        the_list[i + 1][j][1] = (the_list[i + 1][j][1] + total) % modulo
                else:
                    if i + 1 < m:
                        the_list[i + 1][j][1] = (the_list[i + 1][j][1] + r) % modulo
                    if j + 1 < n:
                        the_list[i][j + 1][0] = (the_list[i][j + 1][0] + d) % modulo
        return (the_list[m - 1][n - 1][0] + the_list[m - 1][n - 1][1]) % modulo