from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        dummy_head.next = head

        prev = dummy_head
        current_node = head

        while current_node and current_node.next:

            first_node = current_node
            second_node = current_node.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev = first_node
            current_node = first_node.next

        return dummy_head.next