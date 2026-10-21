class Solution:
    def minOperations(self, s):
        if s == "".join(sorted(s)):
            return 0
        lengthh = len(s)
        if lengthh == 2:
            return -1
        smallest = min(s)
        largest = max(s)
        if s[0] == smallest or s[-1] == largest:
            return 1
        mid = s[1:-1]
        if smallest in mid or largest in mid:
            return 2
        return 3