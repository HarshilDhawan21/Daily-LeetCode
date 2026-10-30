class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for est, e1, e2 in edges:
            graph[est].append((e1, e2))
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]
        while heap:
            cost, node, streak = heapq.heappop(heap)
            if cost > dist[node][streak]:
                continue
            if node == n - 1:
                return cost
            for e1, e2 in graph[node]:
                new_streak = streak + 1 if labels[e1] == labels[node] else 1
                if new_streak > k:
                    continue
                new_dist = cost + e2
                if new_dist < dist[e1][new_streak]:
                    dist[e1][new_streak] = new_dist
                    heapq.heappush(heap, (new_dist, e1, new_streak))
        return -1