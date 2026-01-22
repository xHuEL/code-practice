from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = dict()
        n = len(nums)

        for i in range(n):
            if nums[i] * 2 == target:
                if maps.__contains__(nums[i]):
                    return [i, maps[nums[i]]]

            maps[nums[i]] = i

        for i in range(n):
            other = target - nums[i]
            if maps.__contains__(other) and other != nums[i]:
                return [i, maps[other]]

        return []


