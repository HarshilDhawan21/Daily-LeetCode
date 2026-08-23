class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        adha = n // 2
        s1, c1 = 0, 0
        s2, c2 = 0, 0
        for i in range(adha):
            if num[i] == '?':
                c1 += 1
            else:
                s1 += int(num[i])
        for i in range(adha, n):
            if num[i] == '?':
                c2 += 1
            else:
                s2 += int(num[i])
        if (c1 + c2) % 2 == 1:
            return True 
        bacha = s1 - s2
        ans = (c2 - c1) * 9 // 2 
        return bacha != ans