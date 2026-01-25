# 属于宽度优先遍历，不属于递归
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        queue = [root]
        while len(queue) > 0:
            level_node_list = []
            for node in queue:
                level_node_list.append(node)

            queue = []
            for node in level_node_list:
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            ans.append([node.val for node in level_node_list])

        return ans

