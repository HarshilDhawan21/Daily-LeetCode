class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = best = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc, dec = inc + 1, 1
            elif nums[i] < nums[i-1]:
                dec, inc = dec + 1, 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best 