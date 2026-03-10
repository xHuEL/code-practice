from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        ans = [0 for _ in range(n)]
        for i in range(n):
            inx = (i + k) % n
            # print(nums[inx])
            ans[inx] = nums[i]

        nums.clear()
        for i in range(n):
            nums.append(ans[i])