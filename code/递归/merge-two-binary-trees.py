from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        sums = 0
        left1 = None
        right1 = None
        if root1 is not None:
            sums += root1.val
            left1 = root1.left
            right1 = root1.right

        left2 = None
        right2 = None
        if root2 is not None:
            sums += root2.val
            left2 = root2.left
            right2 = root2.right

        leftTree = self.mergeTrees(left1, left2)
        rightTree = self.mergeTrees(right1, right2)

        newRoot = TreeNode(sums, leftTree, rightTree)
        return newRoot
