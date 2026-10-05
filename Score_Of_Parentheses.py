class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = cnt = 0
        for i, a in enumerate(s):
            if a == '(':
                cnt += 1
            else:
                cnt -= 1
                if s[i-1] == '(':
                    score += 1 << cnt
        return score