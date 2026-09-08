class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        i = 1000
        while i <= n:
            ans += n - i + 1
            i *= 1000
        return ans