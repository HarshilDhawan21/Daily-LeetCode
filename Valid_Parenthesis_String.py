class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0 
        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0