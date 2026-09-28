class Solution:
    def maxDepth(self, s: str) -> int:
        max_dep = 0
        curr_dep = 0
        for char in s:
            if char == "(":
                curr_dep += 1
                max_dep = max(max_dep, curr_dep)
            elif char == ")":
                curr_dep -= 1
        return max_dep       