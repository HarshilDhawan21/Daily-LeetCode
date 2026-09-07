class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(str(n), reverse=True)
        return int(digits[0]) * int(digits[1])