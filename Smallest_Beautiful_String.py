class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        selected = ""
        l = 0
        ones = 0
        for r in range(n):
            if s[r] == '1':
                ones += 1
            while ones == k and l <= r:
                curr = s[l:r+1]
                if selected == "" or len(curr) < len(selected) or (len(curr) == len(selected) and curr < selected):
                    selected = curr
                if s[l] == '1':
                    ones -= 1
                l += 1
        return selected