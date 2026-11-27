class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        min_price = min(price for factor, price in items)
        chosen = [0] * (budget + 1)
        for factor_i, price_i in items:
            copy = 0
            for factor_j, price_j in items:
                if factor_j % factor_i == 0:
                    copy += 1
            for n in range(budget, price_i - 1, -1):
                chosen[n] = max(chosen[n], chosen[n - price_i] + copy)
        best = 0
        for n in range(budget + 1):
            best = max(best, chosen[n] + (budget - n) // min_price)
        return best