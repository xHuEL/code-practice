from typing import List


class Solution:
    def dfs(self, nums: List[int], ans: List[List[int]], res : List[int],
            inx : int, n : int):

        if inx >= n:
            new_list = res[:]
            ans.append(new_list)
            return

        res.append(nums[inx])
        self.dfs(nums, ans, res, inx + 1, n)
        res.remove(nums[inx])

        self.dfs(nums, ans, res, inx + 1, n)






    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        n = len(nums)
        self.dfs(nums, ans, res, 0, n)
        return ans
