from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        flag = True
        if root.left is not None:
            flag &= self.isValidBST(root.left)
            flag &= (root.val > root.left.val)

        if root.right is not None:
            flag &= self.isValidBST(root.right)
            flag &= (root.val < root.right.val)

        return flag

