class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            width = r - l
            smaller = min(height[l], height[r])
            best = max(best, smaller * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
        