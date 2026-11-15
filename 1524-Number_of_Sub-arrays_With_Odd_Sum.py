class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        m = 10**9 + 7
        odd, even = 0, 1
        pre = 0
        ans = 0
        for i in arr:
            pre += i
            if pre % 2:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % m