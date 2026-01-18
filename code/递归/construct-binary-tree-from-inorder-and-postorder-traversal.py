from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 理解递归构造的过程，然后记住就可以，这种类型也就二叉树构造，后面做多了，就慢慢有感觉了
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 and len(postorder) == 0:
            return None

        root = postorder[-1]
        # 在中序遍历中找到root所在的位置, provit前面就是左子树的中序遍历结果，provit后面就是右子树中序遍历的结果
        provit = -1
        n = len(inorder)
        for i in range(n):
            if inorder[i] == root:
                provit = i

        leftTree = self.buildTree(inorder[0:provit], postorder[0:provit])
        rightTree = self.buildTree(inorder[provit + 1:], postorder[provit:-1])
        return TreeNode(root, leftTree, rightTree)

