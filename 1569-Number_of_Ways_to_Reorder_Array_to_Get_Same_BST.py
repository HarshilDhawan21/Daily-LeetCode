from math import comb as main
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        modulo = 10**9 + 7
        def sui(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return main(len(left) + len(right), len(left)) * sui(left) * sui(right) % modulo
        return (sui(nums) - 1) % modulo