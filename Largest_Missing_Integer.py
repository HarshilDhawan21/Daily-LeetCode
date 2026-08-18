class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        c= Counter(nums)
        if k == 1:
            return max((x for x in nums if c[x] == 1), default=-1)
        main = []
        if c[nums[0]] == 1:
            main.append(nums[0])
        if c[nums[-1]] == 1:
            main.append(nums[-1])
        return max(main, default=-1)