class Solution:
    def maxLength(self, nums: list[int]) -> int:
        most = 25200
        n, main = len(nums), 0
        for i in range(n): 
            prod, g, l = 1, 0, 1
            for j in range(i, n): 
                n1 = nums[j]
                prod *= n1
                if prod > most: 
                    break
                g = gcd(g, n1)
                l = l * n1 // gcd(l, n1)
                if prod == g * l:
                    main = max(main, j - i + 1)
        return main