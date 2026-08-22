class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        for i in str(n):
            d = int(i)
            s += d
            p *= d
        return n % (s + p) == 0

