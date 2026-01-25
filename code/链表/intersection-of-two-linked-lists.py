from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 第一种方法：使用map
        visited = {}

        while headA is not None:
            visited[headA] = 1
            headA = headA.next

        while headB is not None:
            if visited.__contains__(headB):
                return headB
            headB = headB.next
        return None