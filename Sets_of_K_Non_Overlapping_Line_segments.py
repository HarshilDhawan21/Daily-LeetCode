class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
            from math import comb as a
            module = 10**9 + 7
            return a(n + k - 1, 2 * k) % module     