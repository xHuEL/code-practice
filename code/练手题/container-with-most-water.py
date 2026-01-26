from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 单调栈经典题目，以第i个线为水的高度，找到左右两边比height[i]高的线
        # 单调栈就是为了找到一个数左右两边的比它大，并且离它最近的数
        stack = []
        n = len(height)

        
