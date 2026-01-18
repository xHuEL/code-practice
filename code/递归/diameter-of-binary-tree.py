from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0

        lh = 0
        if root.left is not None:
            lh = self.dfs(root.left)
            lh += 1

        rh = 0
        if root.right is not None:
            rh = self.dfs(root.right)
            rh += 1

        self.ans = max(self.ans, lh + rh)
        return max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans
