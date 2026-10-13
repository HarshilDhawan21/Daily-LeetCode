class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squ = sorted(i * i for i in nums)
        n = len(squ)
        a = n // 2
        return sum(squ[a:]) - sum(squ[:a])
 