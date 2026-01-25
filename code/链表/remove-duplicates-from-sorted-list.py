from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        def delNode():
            prev.next = cur.next

        while cur is not None:
            if prev is not None:
                if cur.val == prev.val:
                    delNode()
                else:
                    prev = cur
            else:
                prev = cur
            cur = cur.next
        return head