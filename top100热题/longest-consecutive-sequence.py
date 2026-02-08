from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 第一种方法, 排序
        n = len(nums)

        nums.sort()

        ans = 0
        cur_res = 0
        for i in range(n):
            if i == 0:
                cur_res += 1
            else:
                if nums[i] == nums[i - 1] + 1:
                    cur_res += 1
                elif nums[i] == nums[i - 1]:
                    cur_res = cur_res
                else:
                    cur_res = 1

            if cur_res > ans:
                ans = cur_res

        return ans
