class Solution:
    def distinctSubseqII(self, s: str) -> int:
        modulo = 10**9 + 7
        c = 1
        last = [0]*26
        for char in s:
            i = ord(char)-97
            nd = (2*c - last[i]) % modulo
            last[i] = c
            c = nd
        return (c-1) % modulo