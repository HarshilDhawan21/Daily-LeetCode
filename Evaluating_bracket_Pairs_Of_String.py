class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        main = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = s.find(')', i)
                key = s[i+1:j]
                main.append(d.get(key, '?'))
                i = j + 1
            else:
                main.append(s[i])
                i += 1
        return ''.join(main)