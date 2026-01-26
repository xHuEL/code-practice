from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
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

            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

        if catch > 0:
            newNode = ListNode(catch)
            tail.next = newNode

        return head
