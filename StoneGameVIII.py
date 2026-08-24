class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = stones[:]
        for i in range(1, n):
            pre[i] += pre[i - 1]      
        main = pre[n - 1] 
        for i in range(n - 2, 0, -1):
            main = max(main, pre[i] - main)       
        return main