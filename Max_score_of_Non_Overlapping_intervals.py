class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        l = [intervals[i][0] for i in order]
        r = [intervals[i][1] for i in order]
        w = [intervals[i][2] for i in order]
        p = [bisect.bisect_left(r, l[i]) - 1 for i in range(n)]
        dp = [[(0, [])] + [(-1, [])]*4 for _ in range(n+1)]
        for i in range(1, n+1):
            for k in range(5):
                best = dp[i-1][k]
                if k > 0:
                    prev = dp[p[i-1]+1][k-1]
                    if prev[0] >= 0:
                        toat = (prev[0] + w[i-1], sorted(prev[1] + [order[i-1]]))
                        if toat[0] > best[0] or (toat[0] == best[0] and toat[1] < best[1]):
                            best = toat
                dp[i][k] = best
        max_score = max(dp[n][k][0] for k in range(5))
        toats = [dp[n][k][1] for k in range(5) if dp[n][k][0] == max_score]
        return min(toats)