from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0 for i in range(n)]

        for i in range(n):
            if i != 0:
                sums[i] = sums[i - 1] + nums[i]
            else:
                sums[i] = nums[i]

        minval = 0
        maxval = -0xfffffffff
        ans = -0xfffffff
        for i in range(n):
            ans = max(ans, sums[i] - minval)
            minval = min(minval, sums[i])

        return ans

