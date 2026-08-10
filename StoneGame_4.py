class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        data= [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not data[i - j * j]:
                    data[i] = True
                    break
                j += 1
        return data[n]