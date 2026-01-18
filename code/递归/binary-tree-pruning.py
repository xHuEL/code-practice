from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            if root.val == 0:
                return None
            else:
                return root

        leftTree = None
        if root.left is not None:
            leftTree = self.pruneTree(root.left)

        rightTree = None
        if root.right is not None:
            rightTree = self.pruneTree(root.right)

        if leftTree is None and rightTree is None:
            if root.val == 0:
                return None

        root.left = leftTree
        root.right = rightTree
        return root

