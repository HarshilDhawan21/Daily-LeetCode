class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda left: left[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        c = {}
        left = right = 0
        for i in order:
            curr = queries[i]
            while right < len(logs) and logs[right][1] <= curr:
                s = logs[right][0]
                c[s] = c.get(s, 0) + 1
                right += 1
            while left < right and logs[left][1] < curr - x:
                s = logs[left][0]
                c[s] -= 1
                if c[s] == 0:
                    del c[s]
                left += 1
            ans[i] = n - len(c)
        return ans