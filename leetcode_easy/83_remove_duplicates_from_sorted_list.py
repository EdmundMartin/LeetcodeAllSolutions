from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        prev = None
        current_node = head
        while current_node:
            if prev is not None and prev.val == current_node.val:
                prev.next = current_node.next
                current_node = current_node.next
            else:
                prev = current_node
                current_node = current_node.next
        return head