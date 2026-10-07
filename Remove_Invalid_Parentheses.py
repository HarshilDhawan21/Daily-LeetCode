class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left:
                    left -= 1
                else:
                    right += 1
        main = set()
        def dfs(i, l, r, openc, listc):
            if i == len(s):
                if l == 0 and r == 0 and openc == 0:
                    main.add(''.join(listc))
                return
            c = s[i]
            if c == '(' and l > 0:
                dfs(i + 1, l - 1, r, openc, listc)
            elif c == ')' and r > 0:
                dfs(i + 1, l, r - 1, openc, listc)
            listc.append(c)
            if c == '(':
                dfs(i + 1, l, r, openc + 1, listc)
            elif c == ')':
                if openc > 0:
                    dfs(i + 1, l, r, openc - 1, listc)
            else:
                dfs(i + 1, l, r, openc, listc)
            listc.pop()
        dfs(0, left, right, 0, [])
        return list(main)