class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        lower, higher = min(i, j), max(i, j)
        return min(higher + 1, n - lower, (lower + 1) + (n - higher))
