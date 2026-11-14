class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
        best = float('inf')
        for i in range(n):
            for j in range(i + l, min(i + r, n) + 1):
                summ = pre[j] - pre[i]
                if 0 < summ < best:
                    best = summ
        return -1 if best == float('inf') else best