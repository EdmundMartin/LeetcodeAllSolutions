from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 28 ms, faster than 99.56% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.5 MB, less than 56.30% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        current_node = head
        while current_node:
            next = current_node.next
            current_node.next = dummy_head.next
            dummy_head.next = current_node
            current_node = next
        return dummy_head.next


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    result = Solution().reverseList(h)
    print(result.val)

    node = result
    while node:
        print(node.val)
        node = node.next