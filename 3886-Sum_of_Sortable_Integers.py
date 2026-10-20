class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:  
        n = len(nums)
        main = 0
        for s in range(1, n + 1):
            if n % s != 0:
                continue
            sort = True
            max_prev = 0
            for i in range(0, n, s):
                block = nums[i:i + s]
                d = 0
                st_rotation = 0
                for j in range(s):
                    next = (j + 1) % s
                    if block[j] > block[next]:
                        d += 1
                        st_rotation = next
                if d > 1:
                    sort = False
                    break
                mn = block[st_rotation]
                mx = block[st_rotation - 1]
                if mn < max_prev:
                    sort = False
                    break
                max_prev = mx
            if sort:
                main += s
        return main