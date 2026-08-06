class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        s = [False] * n
        s[k] = True
        stk = [k]
        while stk:
            node = stk.pop()
            for nxt in graph[node]:
                if not s[nxt]:
                    s[nxt] = True
                    stk.append(nxt)
        for a, b in invocations:
            if s[b] and not s[a]:
                return list(range(n))
        return [i for i in range(n) if not s[i]]