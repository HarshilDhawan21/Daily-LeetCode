class Solution:
    def romanToInt(self, s: str) -> int:
        vor= {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if vor[s[i]] < vor[s[i + 1]]:
                total -= vor[s[i]]
            else:
                total += vor[s[i]]
        return total + vor[s[-1]]
        
        