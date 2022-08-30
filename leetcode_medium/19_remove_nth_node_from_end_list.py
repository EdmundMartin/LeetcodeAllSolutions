from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        fast = head
        while fast:
            length += 1
            fast = fast.next
        length -= n

        slow = dummy
        while length > 0:
            length -= 1
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(3)
    start.next.next.next = ListNode(4)
    start.next.next.next.next = ListNode(5)

    h = Solution().removeNthFromEnd(start, 2)

    values = []
    while h:
        values.append(h.val)
        h = h.next
    print(values)

    start_two = ListNode(1)
    h = Solution().removeNthFromEnd(start_two, 1)