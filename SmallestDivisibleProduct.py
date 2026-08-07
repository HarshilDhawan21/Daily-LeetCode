class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            a = 1
            b = i
            while b:
                a *= b % 10
                b //= 10
            if a % t == 0:
                return i
            i += 1