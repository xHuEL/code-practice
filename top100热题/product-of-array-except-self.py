from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        L = [1 for _ in range(n + 1)]
        R = [1 for _ in range(n + 1)]
        ans = []

        for i in range(n):
            if i != 0:
                L[i] = L[i - 1] * nums[i]
            else:
                L[i] = nums[i]
        # print(L)

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                R[i] = nums[i]
            else:
                R[i] = R[i + 1] * nums[i]
        # print(R)

        for i in range(n):
            if i != 0:
                ans.append(L[i - 1] * R[i + 1])
            else:
                ans.append(R[i + 1])
        return ans