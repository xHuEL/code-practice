# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def addNode(node: ListNode):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        head : Optional[ListNode] = None
        tail : Optional[ListNode] = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                addNode(list2)
                list2 = list2.next
            elif list2 is None:
                addNode(list1)
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    addNode(list2)
                    list2 = list2.next
                else:
                    addNode(list1)
                    list1 = list1.next
        return head


