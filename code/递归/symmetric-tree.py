from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root1 : Optional[TreeNode], root2 : Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.dfs(root.left, root.right)


