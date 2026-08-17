class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]
        def total(a, b):
            return pre[b + 1] - pre[a]
        data = [[0] * n for _ in range(n)]
        def sc(a, b):
            return total(a, b) + data[a][b]
        NEG = float('-inf')
        l_pt = [i - 1 for i in range(n)]
        l_main = [NEG] * n
        r_pt = [j for j in range(n)]
        r_main = [NEG] * n
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                while l_pt[i] + 1 <= j - 1 and 2 * total(i, l_pt[i] + 1) <= total(i, j):
                    l_pt[i] += 1
                    l_main[i] = max(l_main[i], sc(i, l_pt[i]))
                while r_pt[j] - 1 >= i and 2 * total(r_pt[j], j) <= total(i, j):
                    r_main[j] = max(r_main[j], sc(r_pt[j], j))
                    r_pt[j] -= 1
                best_l = l_main[i] if l_pt[i] >= i else NEG
                best_r = r_main[j] if r_pt[j] <= j - 1 else NEG
                data[i][j] = max(best_l, best_r)
        return data[0][n - 1]
