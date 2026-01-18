from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = preorder[0]
        # 找到root在inorder出现的位置
        n = len(inorder)
        provit = -1
        for i in range(n):
            if inorder[i] == root:
                provit = i

        leftTree = self.buildTree(preorder[1 : 1 + provit], inorder[0 : provit])
        rightTree = self.buildTree(preorder[1 + provit :], inorder[provit + 1 : ])
        rootNode = TreeNode(root, leftTree, rightTree)
        return rootNode

