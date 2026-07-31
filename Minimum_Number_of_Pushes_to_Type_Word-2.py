class Solution:
    def minimumPushes(self, word: str) -> int:
        a= sorted(Counter(word).values(), reverse=True)
        ans= 0
        for i, f in enumerate(a):
             ans+= f * (i // 8 + 1)
        return ans