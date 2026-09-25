class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr):
            fin = []
            curr = {""}
            i, n = 0, len(expr)
            while i < n:
                ch = expr[i]
                if ch == '{':
                    depth = 1
                    j = i + 1
                    while depth > 0:
                        if expr[j] == '{':
                            depth += 1
                        elif expr[j] == '}':
                            depth -= 1
                        j += 1
                    insider = parse(expr[i + 1:j - 1])
                    curr = {a + b for a in curr for b in insider}
                    i = j
                elif ch == ',':
                    fin.append(curr)
                    curr = {""}
                    i += 1
                else:
                    curr = {word + ch for word in curr}
                    i += 1
            fin.append(curr)
            main = set()
            for words in fin:
                main |= words
            return main
        return sorted(parse(expression))