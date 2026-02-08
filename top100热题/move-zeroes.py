from typing import List

# 打卡题
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a, b):
            temp = nums[a]
            nums[a]= nums[b]
            nums[b] = temp

        n = len(nums)
        ll = 0
        for i in range(0, n):
            if nums[i] != 0:
                swap(ll, i)
                ll += 1


