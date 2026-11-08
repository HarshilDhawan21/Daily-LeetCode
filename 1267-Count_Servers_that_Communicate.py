class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row= [sum(r) for r in grid]
        col = [sum(c) for c in zip(*grid)]
        return sum(
            1
            for i, r in enumerate(grid)
            for j, v in enumerate(r)
            if v and (row[i] > 1 or col[j] > 1)
        )