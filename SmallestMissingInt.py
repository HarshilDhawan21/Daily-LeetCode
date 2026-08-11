class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        Sum = nums[0]
        a = 1
        while a < len(nums) and nums[a] == nums[a - 1] + 1:
            Sum += nums[a]
            a += 1
        curr= set(nums)
        s= Sum
        while s in curr:
            s += 1
        return s