class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        xor = 0
        c = 0
        for i in nums:
            xor ^= i
            c+= int(i==0)
        if xor:
            return n
        if c == n:
            return 0
        return n - 1