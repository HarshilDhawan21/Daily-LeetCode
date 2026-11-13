class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        rev = nums[::-1]
        maxx = deque()  
        left = 0
        operation = 0
        main = 0
        for right, new in enumerate(rev):
            while maxx and rev[maxx[-1]] <= new:
                popp = maxx.pop()
                prev = maxx[-1] if maxx else left - 1
                c = popp - prev
                operation += (new - rev[popp]) * c
            maxx.append(right)
            while operation > k:
                curr_maxx = rev[maxx[0]]
                operation -= curr_maxx - rev[left]
                if maxx[0] == left:
                    maxx.popleft()
                left += 1
            main += right - left + 1
        return main