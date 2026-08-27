class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        c = [0]*26
        for i in s: c[ord(i)-97] += 1
        stp = n
        for i in range(n):
            fetched = ord(target[i])-97
            if c[fetched] > 0: c[fetched] -= 1
            else: stp = i; break
        point = n-1 if stp == n else stp
        if stp == n: c[ord(target[n-1])-97] += 1
        i = point
        while i >= 0:
            fetched = ord(target[i])-97
            found = next((j for j in range(fetched+1,26) if c[j]>0), -1)
            if found != -1:
                c[found] -= 1
                bache = ''.join(chr(97+j)*c[j] for j in range(26))
                return target[:i] + chr(97+found) + bache
            if i == 0: break
            c[ord(target[i-1])-97] += 1
            i -= 1
        return ""