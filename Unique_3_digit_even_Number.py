class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        count = 0
        for a in range(1, 10):
            if freq[a] == 0:
                continue
            for b in range(0, 10):
                if freq[b] == 0:
                    continue
                for c in range(0, 10, 2):
                    if freq[c] == 0:
                        continue
                    needed = Counter([a, b, c])
                    if all(freq[d] >= needed[d] for d in needed):
                        count += 1
        return count