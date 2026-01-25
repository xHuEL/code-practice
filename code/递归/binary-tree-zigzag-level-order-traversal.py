from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        queue = [root]
        level = 0
        while len(queue) > 0:
            level_node_list = [node for node in queue]
            queue = []
            for node in level_node_list:
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level % 2 == 1:
                level_val_list = [node.val for node in reversed(level_node_list)]
            else:
                level_val_list = [node.val for node in level_node_list]
            ans.append(level_val_list)
            level += 1

        return ans
