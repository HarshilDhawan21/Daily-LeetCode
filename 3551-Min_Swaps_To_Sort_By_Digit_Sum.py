class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def dsum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        n = len(nums)
        goal = sorted(range(n), key=lambda i: (dsum(nums[i]), nums[i]))
        done = [False] * n
        iteration = 0
        for i in range(n):
            if not done[i]:
                iteration += 1
                j = i
                while not done[j]:
                    done[j] = True
                    j = goal[j]
        return n - iteration