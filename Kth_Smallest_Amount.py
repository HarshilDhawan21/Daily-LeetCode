class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        def lcm(a, b):
            return a * b // gcd(a, b)
        def count_le(x):
            total = 0
            for i in range(1, 1 << n):
                l = 1
                c = 0
                over = False
                for j in range(n):
                    if i & (1 << j):
                        l = lcm(l, coins[j])
                        c += 1
                        if l > x:
                            over = True
                            break
                if over:
                    continue
                s = 1 if c % 2 == 1 else -1
                total += s * (x // l)
            return total
        low, high = 1, min(coins) * k
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low