class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        selected = 0
        for i, a in enumerate(s):
            if a == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    selected = max(selected, i - stk[-1])
        return selected