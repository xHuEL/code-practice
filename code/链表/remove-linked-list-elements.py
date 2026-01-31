from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None

        def delNode(node: ListNode):
            nonlocal prev, head
            if prev is not None:
                prev.next = node.next
            else:
                head = node.next

        while cur is not None:
            if cur.val == val:
                delNode(cur)
            else:
                prev = cur
            cur = cur.next
        return head
