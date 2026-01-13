from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 首先通过排序来实现
        sorted(nums)
        print(nums)
        n = len(nums)
        ans = []
        cnt = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                cnt = cnt + 1
            else:
                if cnt >= n / 3:
                    ans.append(nums[i - 1])
                cnt = 0
        if cnt >= n / 3:
            ans.append(nums[n - 1])
        return ans

