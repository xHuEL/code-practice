from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        cur = head

        head = None
        tail = None

        def addNode(node):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node


        while cur is not None:
            group = 0
            for i in range(k):
                if cur is not None:
                    stack.append(cur)
                    cur = cur.next
                    group += 1


            if group == k:
                while len(stack) > 0:
                    node = stack[-1]
                    node.next = None
                    addNode(node)

                    stack.pop()
            else:
                while len(stack) > 0:
                    node = stack[0]
                    node.next = None
                    addNode(node)

                    stack.pop(0)

        return head



