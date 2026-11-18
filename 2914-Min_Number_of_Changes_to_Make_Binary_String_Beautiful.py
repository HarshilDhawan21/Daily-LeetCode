class Solution:
    def minChanges(self, s: str) -> int:
        c = 0
        for i in range(0, len(s), 2):
            a1 = s[i]
            a2 = s[i + 1]
            if a1 != a2:
                c += 1
        return c