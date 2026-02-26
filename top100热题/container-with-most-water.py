from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        n = len(height)
        L = 0
        R = n - 1

        while L < R:
            area = min(height[R], height[L]) * (R - L)
            if area > ans:
                ans = area

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return ans