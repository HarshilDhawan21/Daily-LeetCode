class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []
        a = [0] * (n + 1)
        a[n] = m
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            a[i] = j
        ans = []
        j = 0
        done = False
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not done and a[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                done = True
        return ans if j == m else []