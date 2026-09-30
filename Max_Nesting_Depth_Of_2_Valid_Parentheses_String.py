class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        main, dep = [], 0
        for i in seq:
            if i == '(':
                dep += 1
                main.append(dep % 2)
            else:
                main.append(dep % 2)
                dep -= 1
        return  main