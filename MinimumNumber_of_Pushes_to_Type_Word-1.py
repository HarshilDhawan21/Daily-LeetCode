class Solution:
    def minimumPushes(self,word: str) -> int:
        a= len(word)
        ans= 0
        for i in range(a):
            ans+=(i // 8 + 1)
        return ans