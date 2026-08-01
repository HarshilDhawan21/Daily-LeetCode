class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        data= nums[:]
        for i in range(2, n + 1):
            for j in range(n - i + 1):
                l = j + i - 1
                data[j] = max(nums[j] - data[j+1], nums[l] - data[j])
        return data[0] >= 0