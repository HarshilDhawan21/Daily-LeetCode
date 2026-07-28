class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        half = []
        mid = ''
        for i in sorted(c):
            if c[i] % 2:
                mid = i
            half.append(i * (c[i] // 2))
        pre = ''.join(half)
        return pre + mid + pre[::-1]
