class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        count9 = sum // 9
        remains = sum % 9
        main = "9" * count9
        if remains:
            main += str(remains)
        count0 = num - len(main)
        main += "0" * count0
        return main