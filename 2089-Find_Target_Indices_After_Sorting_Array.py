class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        st = 0
        c = 0
        for i in nums:
            if i < target:
                st += 1
            elif i == target:
                c += 1
        return list(range(st, st + c))