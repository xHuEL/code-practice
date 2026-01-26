import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        delta = sys.maxsize
        ans = sys.maxsize
        nums.sort()

        for first in range(n):
            now_target = target - nums[first]

            second = first + 1
            third = n - 1
            while second < third:
                if delta > abs(nums[second] + nums[third] + nums[first] - target):
                    delta = abs(nums[second] + nums[third] + nums[first] - target)
                    ans = nums[second] + nums[third] + nums[first]
                    # print(delta, nums[first], nums[second], nums[third])

                if nums[second] + nums[third] < now_target:
                    second += 1
                elif nums[second] + nums[third] > now_target:
                    third -= 1
                else:
                    return target

        return ans