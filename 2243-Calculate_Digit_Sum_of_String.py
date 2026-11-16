class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            a = ""
            for i in range(0, len(s), k):
                grp = s[i:i+k]
                total = 0
                for ch in grp:
                    total += int(ch)
                a += str(total)
            s = a
        return s