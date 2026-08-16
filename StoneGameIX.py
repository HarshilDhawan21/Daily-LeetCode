class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c=[0, 0, 0]
        for i in stones:
            c[i % 3] += 1
        if c[0] % 2 == 0:
            return c[1] >= 1 and c[2] >= 1
        else:
            return abs(c[1] - c[2]) > 2