from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maps = {}
        n = len(nums)

        for i in range(n):
            if maps.__contains__(nums[i]):
                maps[nums[i]] = maps[nums[i]] + 1
            else:
                maps[nums[i]] = 1

        ans = 0
        for key in maps.keys():
            v1 = maps[key]

            if maps.__contains__(key + 1):
                v2 = maps[key + 1]
                if v1 + v2 > ans:
                    ans = v1 + v2
        return ans

