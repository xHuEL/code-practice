import sys
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ll = 0
        rr = 0

        n = len(nums)
        cur_window_sum = 0
        ans = sys.maxsize
        while rr < n:
            if cur_window_sum >= target:
                ll += 1
                cur_window_sum = cur_window_sum - nums[ll]

            cur_window_sum += nums[rr]
            rr = rr + 1

            if cur_window_sum >= target:
                print(ll, rr, cur_window_sum)
                ans = min(ans, rr - ll)

        return ans

