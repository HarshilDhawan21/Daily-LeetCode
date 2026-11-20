class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        longest = {}
        for x in nums:
            longest[x + 1] = longest.get(x, 0) + 1
            longest[x] = longest.get(x - 1, 0) + 1
        return max(longest.values())