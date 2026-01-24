# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 堆栈
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next

        def addNode(node):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        head = None
        tail = None
        while len(stack) > 0:
            cur = stack[-1]
            cur.next = None
            stack.pop()

            addNode(cur)

        return head


