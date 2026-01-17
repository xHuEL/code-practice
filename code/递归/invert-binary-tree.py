from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # 后序遍历
        leftTree: Optional[TreeNode] = self.invertTree(root.left)
        rightTree: Optional[TreeNode] = self.invertTree(root.right)

        root.left = rightTree
        root.right = leftTree

        return root
