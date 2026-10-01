class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', ']': '[', '}': '{'}
        stk = []
        for i in s:
            if i in pair:
                if not stk or stk.pop() != pair[i]:
                    return False
            else:
                stk.append(i)
        return not stk