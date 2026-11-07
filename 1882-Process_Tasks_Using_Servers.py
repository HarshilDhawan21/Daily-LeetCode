class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, ind) for ind, w in enumerate(servers)]
        heapq.heapify(free)
        almost = []
        ans = []
        ct = 0
        for at, pt in enumerate(tasks):
            ct = max(ct, at)
            if not free and almost[0][0] > ct:
                ct = almost[0][0]    
            while almost and almost[0][0] <= ct:
                _, w, ind = heapq.heappop(almost)
                heapq.heappush(free, (w, ind))
            w, ind = heapq.heappop(free)
            ans.append(ind)
            heapq.heappush(almost, (ct + pt, w, ind))
        return ans