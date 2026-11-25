class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        m = (1 << 61) - 1
        R = random.randint(10**5, m - 1)
        preh, poww = [0]*(n+1), [1]*(n+1)
        for i, j in enumerate(nums):
            preh[i+1] = (preh[i]*R + j) % m
            poww[i+1] = poww[i]*R % m
        def alr(L):
            c = {}
            for i in range(n - L + 1):
                k = (preh[i+L] - preh[i]*poww[L]) % m
                c[k] = c.get(k, 0) + 1
            return 1 in c.values()
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if alr(mid): high = mid
            else: low = mid + 1
        return low