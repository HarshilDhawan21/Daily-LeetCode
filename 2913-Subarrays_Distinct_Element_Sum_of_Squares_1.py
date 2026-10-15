class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            curr = set()
            for j in range(i, n):
                curr.add(nums[j])
                c += len(curr) ** 2
        return c