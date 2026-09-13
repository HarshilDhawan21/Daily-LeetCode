class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        cor1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        cor2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        shiftc = {}
        for row1, col1 in cor1:
            for row2, col2 in cor2:
                shift = (row1 - row2, col1 - col2)
                shiftc[shift] = shiftc.get(shift, 0) + 1
        return max(shiftc.values(), default=0)    