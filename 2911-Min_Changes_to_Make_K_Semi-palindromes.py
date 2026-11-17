class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        divis = [[d for d in range(1, L) if L % d == 0] for L in range(n + 1)]
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divis[L]:
                    c = 0
                    cnt = L // d
                    for r in range(d):
                        a = i + r
                        b = a + (cnt - 1) * d
                        while a < b:
                            if s[a] != s[b]:
                                c += 1
                            a += d
                            b -= d
                    best = min(best, c)
                cost[i][j] = best
        ans = [[INF] * (n + 1) for _ in range(k + 1)]
        ans[0][0] = 0
        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                for p in range(2 * (j - 1), i - 1):
                    v = ans[j - 1][p] + cost[p][i - 1]
                    if v < ans[j][i]:
                        ans[j][i] = v
        return ans[k][n]