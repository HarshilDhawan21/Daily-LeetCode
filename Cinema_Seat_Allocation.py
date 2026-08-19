class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= (1 << (seat - 2))
        l= 0b00001111
        m= 0b00111100
        r = 0b11110000
        ans = 2 * (n - len(rows))
        for i in rows.values():
            if (i & l) == 0 or (i & r) == 0:
                ans += 2 if (i & l) == 0 and (i & r) == 0 else 1
            elif (i & m) == 0:
                ans += 1
        return ans