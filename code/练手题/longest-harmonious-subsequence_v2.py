from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        if n <= 0:
            return 0

        ll = 0
        r = 0
        ans = 0
        while r < n:
            r_start = r
            while r < n and nums[r] == nums[r - 1]:
                r += 1

            if nums[r - 1] - nums[ll] == 1:
                ans = max(ans, r - ll)
                ll = r_start
            elif nums[r - 1] != nums[ll]:
                ll = r_start
        return ans

