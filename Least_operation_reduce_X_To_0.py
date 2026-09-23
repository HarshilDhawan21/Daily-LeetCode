class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tgt = sum(nums) - x
        if tgt < 0:
            return -1
        if tgt == 0:
            return len(nums)
        toplen = -1
        currs = 0
        l = 0
        for r in range(len(nums)):
            currs += nums[r]
            while currs > tgt and l <= r:
                currs -= nums[l]
                l += 1
            if currs == tgt:
                toplen = max(toplen, r - l + 1)
        return len(nums) - toplen if toplen != -1 else -1