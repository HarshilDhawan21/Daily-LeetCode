class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        main = [float('inf')] * (n + 1)
        ans = float('inf')
        left = 0
        sum = 0
        for right in range(n):
            sum += arr[right]
            while sum > target:
                sum -= arr[left]
                left += 1
            main[right + 1] = main[right]
            if sum == target:
                length = right - left + 1
                if main[left] != float('inf'):
                    ans = min(ans, main[left] + length)
                main[right + 1] = min(main[right + 1], length)
        return ans if ans != float('inf') else -1