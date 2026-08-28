class Solution:
    def smallestPalindrome(self, s: str, target: str) -> str:
        n = len(s)
        c = [0] * 26
        for ch in s:
            c[ord(ch) - 97] += 1
        odd = [i for i in range(26) if c[i] % 2]
        if len(odd) > 1 or (len(odd) == 1) != (n % 2 == 1):
            return ""
        mid = chr(97 + odd[0]) if odd else ""
        half_c = [c // 2 for c in c]
        h = n // 2
        target_half = target[:h]
        def fill_smallest(left_over):
            return ''.join(chr(97 + i) * left_over[i] for i in range(26))
        def assembling(first_half):
            return first_half + mid + first_half[::-1]
        def solving(i, chosen, left_over):
            if i == h:
                candidate = assembling(''.join(chosen))
                return candidate if candidate > target else None
            tgt = ord(target_half[i]) - 97
            if left_over[tgt] > 0:
                left_over[tgt] -= 1
                chosen.append(chr(97 + tgt))
                main = solving(i + 1, chosen, left_over)
                chosen.pop()
                left_over[tgt] += 1
                if main is not None:
                    return main
            for c in range(tgt + 1, 26):
                if left_over[c] > 0:
                    left_over[c] -= 1
                    first_half = ''.join(chosen) + chr(97 + c) + fill_smallest(left_over)
                    left_over[c] += 1
                    return assembling(first_half)
            return None
        main = solving(0, [], half_c[:])
        return main if main is not None else ""