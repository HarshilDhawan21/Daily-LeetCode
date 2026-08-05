class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        data = [0, 0, 0, 0]
        for i in range(n - 1, -1, -1):
            total = 0
            best = float('-inf')
            for j in range(3):
                if i + j >= n:
                    break
                total += stoneValue[i + j]
                best = max(best, total - data[(i + j + 1) % 4])
            data[i % 4] = best
        res = data[0]
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"

