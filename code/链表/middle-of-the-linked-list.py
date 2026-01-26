from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur is not None:
            cur = cur.next
            n += 1

        mid = int(n / 2)
        cur = head
        for i in range(mid):
            cur = cur.next

        return cur

