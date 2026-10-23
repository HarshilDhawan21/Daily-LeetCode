class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, a in enumerate(nums):
            if a != i:
                k &= a
        return 0 if k == -1 else k