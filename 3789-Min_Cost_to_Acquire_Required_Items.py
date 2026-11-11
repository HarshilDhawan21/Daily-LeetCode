class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mini = min(need1, need2)
        a = need1 * cost1 + need2 * cost2
        b = mini * costBoth + (need1 - mini) * cost1 + (need2 - mini) * cost2
        c = max(need1, need2) * costBoth
        return min(a, b, c)