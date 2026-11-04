class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        sortted = sorted(set(nums))
        ind = {v: i + 1 for i, v in enumerate(sortted)}
        m = len(sortted)
        countTree = [0] * (m + 1)
        sumTree = [0] * (m + 1)
        def update(i, c, s):
            while i <= m:
                countTree[i] += c
                sumTree[i] += s
                i += i & -i
        top = 1 << (m.bit_length() - 1)
        sma_median = (x + 1) // 2
        cost = [0] * (n - x + 1)
        winsum = 0
        for i in range(n):
            update(ind[nums[i]], 1, nums[i])
            winsum += nums[i]
            if i >= x:
                update(ind[nums[i - x]], -1, -nums[i - x])
                winsum -= nums[i - x]
            if i >= x - 1:
                pos = 0
                countBelow = 0
                sumBelow = 0
                step = top
                while step > 0:
                    nxt = pos + step
                    if nxt <= m and countBelow + countTree[nxt] < sma_median:
                        pos = nxt
                        countBelow += countTree[nxt]
                        sumBelow += sumTree[nxt]
                    step >>= 1
                median = sortted[pos]
                sumAbove = winsum - sumBelow
                countAbove = x - countBelow
                cost[i - x + 1] = (median * countBelow - sumBelow) + (sumAbove - median * countAbove)
        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            curr = [INF] * (n + 1)
            for i in range(x, n + 1):
                skip = curr[i - 1]
                take = prev[i - x] + cost[i - x]
                curr[i] = min(skip, take)
            prev = curr
        return prev[n]