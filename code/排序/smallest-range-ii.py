from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return 0

        ans = nums[n - 1] - nums[0]
        
