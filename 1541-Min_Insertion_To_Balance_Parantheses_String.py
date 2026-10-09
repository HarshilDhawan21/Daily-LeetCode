class Solution:
    def minInsertions(self, s: str) -> int:
        main = 0
        needed = 0
        for i in s:
            if i == '(':
                if needed % 2 == 1:
                    main += 1
                    needed -= 1
                needed += 2
            else:
                needed -= 1
                if needed == -1:
                    main += 1
                    needed = 1
        return main + needed