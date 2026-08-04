class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi, mx = min(nums), max(nums)
        s= set(nums)
        ans = []
        for i in range(mi, mx + 1):     
            if i not in s:
                ans.append(i)
        return ans