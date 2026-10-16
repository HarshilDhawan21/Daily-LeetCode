class RangeSumTracker:
    def __init__(self, s: int):
        self.s = s
        self.t1 = defaultdict(int)
        self.t2 = defaultdict(int)
    def _lowbit(self, pos: int) -> int:
        return pos & -pos
    def r_add(self, left: int, right: int, val: int) -> None:
        self._point_add(left, val)
        self._point_add(right + 1, -val)
    def r_sum(self, left: int, right: int) -> int:
        return self._presum(right) - self._presum(left - 1)
    def _point_add(self, pos: int, val: int) -> None:
        pos += 1
        original_pos = pos
        while pos <= self.s:
            self.t1[pos] += val
            self.t2[pos] += (original_pos - 1) * val
            pos += self._lowbit(pos)
    def _presum(self, pos: int) -> int:
        pos += 1
        if pos > self.s:
            pos = self.s
        original_pos = pos
        c = 0
        while pos > 0:
            c += original_pos * self.t1[pos] - self.t2[pos]
            pos -= self._lowbit(pos)
        return c
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        modulo = 10**9 + 7
        main = 0
        curr_sq_sum = 0
        distinct_c = RangeSumTracker(n + 10)
        last_idx = {}
        for right, val in enumerate(nums):
            left = last_idx.get(val, -1) + 1
            window_sum = distinct_c.r_sum(left, right)
            curr_sq_sum = (curr_sq_sum + 2 * window_sum + (right - left + 1)) % modulo
            main = (main + curr_sq_sum) % modulo
            distinct_c.r_add(left, right, 1)
            last_idx[val] = right
        return main