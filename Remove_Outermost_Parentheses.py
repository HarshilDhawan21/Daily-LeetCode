class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        main = []
        c = 0
        for i in s:
            if i == '(':
                if c > 0:
                    main.append(i)
                c += 1
            else:
                c -= 1
                if c > 0:
                    main.append(i)
        return ''.join(main)