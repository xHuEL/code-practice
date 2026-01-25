from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(a: ListNode, b: ListNode):
            temp = a.val
            a.val = b.val
            b.val = temp

        if head is None:
            return None

        prev = None
        cur = head
        n = 0

        while cur is not None:
            temp = cur
            cur = cur.next

            if prev is not None:
                if n % 2:
                    swap(prev, temp)
            prev = temp
            n += 1

        return head