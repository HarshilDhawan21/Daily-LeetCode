class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        main = []
        def yo(curr, cs, ce):
            if len(curr) == 2 * n:
                main.append(curr)
                return
            if cs < n:
                yo(curr + "(", cs + 1, ce)
            if ce < cs:
                yo(curr + ")", cs, ce + 1)
        yo("", 0, 0)
        return main