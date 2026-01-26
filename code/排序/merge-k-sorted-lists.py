from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def addNode(node):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        # 优先队列来排序，后面堆排序的时候，重新做一次
        def findMin(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            minNode = None
            minNodePos = -1
            n = len(lists)
            for i in range(n):
                node = lists[i]
                if node is None:
                    continue

                if minNode is None:
                    minNode = node
                    minNodePos = i
                else:
                    if minNode.val > node.val:
                        minNode = node
                        minNodePos = i

            if minNode is not None:
                node = minNode.next
                lists[minNodePos] = node

            return minNode


        head = None
        tail = None
        while True:
            minNode = findMin(lists)
            if minNode is None:
                break

            addNode(minNode)
        return head
