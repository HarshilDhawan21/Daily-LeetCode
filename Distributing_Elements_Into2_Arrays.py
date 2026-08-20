class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        first = [nums[0]]
        second = [nums[1]]
        for i in range(2, len(nums)):
            if first[-1] > second[-1]:
                first.append(nums[i])
            else:
                second.append(nums[i])
        return first + second
        