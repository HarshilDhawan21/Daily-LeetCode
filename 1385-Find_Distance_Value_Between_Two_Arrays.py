class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        c = 0
        for i in arr1:
            j = bisect_left(arr2, i)
            btw = False
            if j < len(arr2) and arr2[j] - i <= d:
                btw = True
            if j > 0 and i - arr2[j-1] <= d:
                btw = True
            if not btw:
                c += 1
        return c