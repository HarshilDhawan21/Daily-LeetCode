class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        main = float('inf')
        rise = all(nums[(zero + i) % n] == i for i in range(n))
        if rise:
            if zero == 0:
                main = 0
            else:
                a = zero
                b = n - zero + 2
                main = min(a, b)
        fall = all(nums[(zero - i) % n] == i for i in range(n))
        if fall:
            a = 1 + n - 1 - zero
            b = 1 + (zero + 1) % n
            main = min(main, a, b)
        return -1 if main == float('inf') else main