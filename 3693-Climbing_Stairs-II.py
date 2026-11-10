class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        min_cost = [0] * (n + 1)
        for i in range(1, n + 1):
            best = min_cost[i - 1] + costs[i - 1] + 1
            if i >= 2:
                best = min(best, min_cost[i - 2] + costs[i - 1] + 4)
            if i >= 3:
                best = min(best, min_cost[i - 3] + costs[i - 1] + 9)
            min_cost[i] = best
        return min_cost[n]