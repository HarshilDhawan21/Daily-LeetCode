class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid), len(grid[0])
        total=m * n
        k%= total
        fl=[]
        for i in range(m):
            for j in range(n):
                fl.append(grid[i][j])
        rotated=[0]*total
        for idx in range(total):
            new_idx = (idx + k) % total
            rotated[new_idx] = fl[idx]
        res=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(rotated[i * n + j])
            res.append(row)
        return res