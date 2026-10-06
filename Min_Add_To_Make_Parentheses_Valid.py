class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        closed = 0  
        for i in s:
            if i == '(':
                open += 1
            elif open:
                open -= 1
            else:
                closed += 1
        return open + closed