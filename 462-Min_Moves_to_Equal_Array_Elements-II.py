class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        c = 0
        for n in nums:
            c += abs(n - mid)
        return c    