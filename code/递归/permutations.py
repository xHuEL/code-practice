from typing import List


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def dfs(self, nums: List[int], inx: int, one_ans: List[int], ans: List[List[int]]):
        if inx >= len(nums):
            ans.append(one_ans[:])
            return

        n = len(nums)
        for i in range(inx, n):
            self.swap(nums, inx, i)
            one_ans.append(nums[inx])
            self.dfs(nums, inx + 1, one_ans, ans)
            one_ans.pop()
            self.swap(nums, inx, i)

    # 排序，组合，子集都是很经典回溯求解问题
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
