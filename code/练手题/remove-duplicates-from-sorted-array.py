from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        ll = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue

            else:
                nums[ll + 1] = nums[i]
                ll += 1
        return ll