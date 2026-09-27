class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [""]
        for i in s:
            if i == '(':
                stk.append("")
            elif i == ')':
                top = stk.pop()[::-1]
                stk[-1] += top
            else:
                stk[-1] += i
        return stk[0]