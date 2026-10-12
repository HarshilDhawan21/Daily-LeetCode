class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        modulo = 10**9 + 7
        c = [0] * 31
        for i in nums:
            for j in range(31):
                if i >> j & 1:
                    c[j] += 1
        main = 0
        for r in range(k):
            curr = 0
            for j in range(31):
                if c[j] > 0:
                    curr |= 1 << j
                    c[j] -= 1
            main = (main + curr * curr) % modulo
        return main