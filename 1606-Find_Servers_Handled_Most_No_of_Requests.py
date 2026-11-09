class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))
        busy = []
        cnt = [0] * k
        for i, (at, pt) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= at:
                _, s = heapq.heappop(busy)
                free.add(s)
            if not free:
                continue
            ind = free.bisect_left(i % k)
            if ind == len(free):
                ind = 0
            s = free[ind]
            free.remove(s)
            cnt[s] += 1
            heapq.heappush(busy, (at + pt, s))
        m = max(cnt)
        return [i for i, c in enumerate(cnt) if c == m]