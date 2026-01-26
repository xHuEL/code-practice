from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        maps = dict()
        ans = []
        for i in range(n):
            target = -nums[i]
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            second = i + 1
            third = n - 1
            while second < third:
                if nums[second] + nums[third] < target:
                    second += 1
                elif nums[second] + nums[third] == target:
                    ans.append([nums[i], nums[second], nums[third]])
                    t = (nums[i], nums[second], nums[third])
                    if not maps.__contains__(t):
                        maps[t] = 1
                    second += 1
                    third -= 1
                else:
                    third -= 1

        return ans