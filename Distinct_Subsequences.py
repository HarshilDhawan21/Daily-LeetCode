class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s1, t1 = len(s), len(t)
        if t1 > s1:
            return 0
        changes = [0] * (t1 + 1)
        changes[0] = 1
        for i in range(1, s1 + 1):
            for j in range(min(i, t1), 0, -1):
                if s[i-1] == t[j-1]:
                    changes[j] += changes[j-1]
        return changes[t1]