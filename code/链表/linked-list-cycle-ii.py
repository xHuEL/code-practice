from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # 初始化快慢指针都在head
        slow = fast = head

        # 第一阶段：检测是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # 有环
                # 第二阶段：找到环的入口
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # 返回环的入口节点

        return None  # 无环


