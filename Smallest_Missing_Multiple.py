class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        c=set(nums)
        i=1
        while True:
            ans=k*i
            if ans not in c:
                return ans
            i+=1