class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s, 1):
            total += (123 - ord(c)) * i
        return total