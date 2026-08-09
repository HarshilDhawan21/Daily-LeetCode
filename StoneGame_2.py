class Solution:
    def stoneGameII(self, piles:List[int]) -> int:
        n = len(piles)
        suf_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_sum[i] = suf_sum[i + 1] + piles[i]
        data= [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(1, n + 1):
                if i + 2 * j >= n:
                    data[i][j] = suf_sum[i]
                else:
                    a = 0
                    for X in range(1, 2 * j + 1):
                        a = max(a, suf_sum[i] - data[i + X][max(j, X)])
                    data[i][j] = a
        return data[0][1]
        