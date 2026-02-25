from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列简单的应用
        # 队列是一个先进先出的数据结构
        # 解决k长度区间的最值问题：
        # https://oi-wiki.org/ds/monotonous-queue/
        # https://zhuanlan.zhihu.com/p/346354943 这两个解释都比较好

        n = len(nums)

        # 队列中保存的是数组的索引值，维护索引的原因是题目要求求出k长度区间的最值。
        # 要使用这个索引值来界定k长度的区间
        queue = []

        # 往队列中添加内容
        def push(inx):
            while len(queue) != 0 and nums[queue[-1]] < nums[inx]:
                queue.pop(-1)
            queue.append(inx)

        def pop(inx):
            while len(queue) != 0 and inx - queue[0] + 1 > k:
                queue.pop(0)

        ans = []
        for i in range(0, n):
            if i < k - 1:
                push(i)
            else:
                push(i)
                pop(i)
                ans.append(nums[queue[0]])

        return ans



