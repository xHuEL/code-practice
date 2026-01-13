from typing import List


class Solution:
    def swap(self, nums : List[int], a : int, b : int):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 三色排序
        n = len(nums)
        i = 0
        ll = 0
        r = n - 1
        while i < n:
            if nums[i] == 0:
                self.swap(nums, i, ll)
                ll += 1
            elif nums[i] == 2:
                self.swap(nums, i, r)
                r -= 1
            i += 1

