class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        Endmin = [0] * n
        Endmin[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            Endmin[i] = min(Endmin[i+1], nums[i])
        Startmax = nums[0]
        for i in range(n):
            Startmax = max(Startmax, nums[i])
            if Startmax - Endmin[i] <= k:
                return i
        return -1
        