class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first, last = {}, {}
        for i, j in enumerate(s):
            first.setdefault(j, i)
            last[j] = i
        def check(i):
            a = last[s[i]]
            b = i
            while b <= a:
                if first[s[b]] < i:
                    return -1
                a = max(a, last[s[b]])
                b += 1
            return a
        main, prev_end = [], -1
        for i, j in enumerate(s):
            if i != first[j]:
                continue
            a = check(i)
            if a == -1:
                continue
            if i > prev_end:
                main.append(s[i:a+1])
            else:
                main[-1] = s[i:a+1]
            prev_end = a
        return main