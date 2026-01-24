# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next

        # 删除第N个节点
        cur = None
        tail = None
        while len(stack) > 0:

            n -= 1
            if n == 0:
                stack.pop()
                continue
            else:
                cur = stack[-1]
                cur.next = None
                stack.pop()
                cur.next = tail
                tail = cur

        return cur

