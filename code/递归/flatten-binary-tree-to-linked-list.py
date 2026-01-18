# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 先序遍历的堆栈实现
        if root is None:
            return

        stack = []
        stack.append(root)
        end = None
        while len(stack) > 0:
            top = stack[-1]
            stack.pop()

            if top.right is not None:
                stack.append(top.right)

            if top.left is not None:
                stack.append(top.left)

            if end:
                end.left = None
                end.right = top

            end = top

