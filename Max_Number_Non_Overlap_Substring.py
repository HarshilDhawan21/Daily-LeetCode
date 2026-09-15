class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        main = [0] * (n + 1)
        def _(i, j):
            return s[i:j+1] == s[i:j+1][::-1]
        for i in range(1, n + 1):
            main[i] = main[i - 1]
            for l in (k, k + 1):
                st = i - l
                if st >= 0 and _(st, i - 1):
                    main[i] = max(main[i], main[st] + 1)
                    break
        return main[n]   