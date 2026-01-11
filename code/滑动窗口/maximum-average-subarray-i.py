from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0.0

        n = len(nums)
        ll = 0
        rr = min(ll + k, n)
        ans = 0.0

        for i in range(ll, rr):
            sum += nums[i]
            ans = sum

        while rr < n:
            ll += 1
            rr += 1

            sum -= nums[ll - 1]
            sum += nums[rr - 1]

            if ans < sum:
                ans = sum

        return ans / k
