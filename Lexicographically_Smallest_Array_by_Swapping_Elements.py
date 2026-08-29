class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sort = sorted(range(n), key=lambda i: nums[i])
        main = [0] * n
        st = 0
        for end in range(1, n + 1):
            if end == n or nums[sort[end]] - nums[sort[end - 1]] > limit:
                grp = sorted(sort[st:end])
                for j, i in enumerate(grp):
                    main[i] = nums[sort[st + j]]
                st = end
        return main

            