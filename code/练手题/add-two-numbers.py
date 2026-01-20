from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        last = None
        catch = 0
        while l1 is not None or l2 is not None:
            newNode = ListNode(catch)
            if l1 is not None:
                newNode.val += l1.val
                l1 = l1.next

            if l2 is not None:
                newNode.val += l2.val
                l2 = l2.next

            catch = int(newNode.val / 10)
            newNode.val = int(newNode.val % 10)

            if ans is None:
                ans = newNode
                last = newNode
            else:
                last.next = newNode
                last = newNode

        if catch > 0:
            newNode = ListNode(catch)
            last.next = newNode

        return ans
