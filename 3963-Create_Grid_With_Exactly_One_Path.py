class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        thegrid = [['#'] * n for _ in range(m)]
        for i in range(m):
            thegrid[i][0] = '.'
        for j in range(n):
            thegrid[m - 1][j] = '.'
        return ["".join(row) for row in thegrid]