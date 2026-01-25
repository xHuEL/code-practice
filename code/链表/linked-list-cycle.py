from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        if head is None:
            return False

        slow = head
        if slow is None:
            return False

        fast = slow.next
        if fast is None:
            return False

        while True:
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next
            if fast is None:
                return False

            fast = fast.next
            if fast is None:
                return False


