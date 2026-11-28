class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        c = [0] * (n + 1)
        for f, _ in items:
            c[f] += 1
        mult = [0] * (n + 1)
        for i in range(1, n + 1):
            mult[i] = sum(c[i::i])
        m = min(p for _, p in items)
        cand = sorted((p, mult[f] - 1) for f, p in items if mult[f] > 1)
        ans, remains = 0, budget
        for p, x in cand:
            if p >= 2 * m or p > remains:
                break
            _ = min(x, remains // p)
            ans += 2 * _
            remains -= _ * p
        return ans + remains // m