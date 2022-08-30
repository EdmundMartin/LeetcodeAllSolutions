from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iterate_linked_list(head: ListNode) -> List[int]:
    current = head
    results = []
    while current:
        results.append(current.val)
        current = current.next
    return results


def reverse_linked_list(head: ListNode) -> ListNode:
    dummy_node = ListNode(0)
    current = head
    while current:
        next_node = current.next
        current.next = dummy_node.next
        dummy_node.next = current
        current = next_node
    return dummy_node.next


# Runtime: 1046 ms, faster than 69.13% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 32.4 MB, less than 91.14% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        in_order = iterate_linked_list(head)
        new_head = reverse_linked_list(head)
        rev_order = iterate_linked_list(new_head)
        return in_order == rev_order
