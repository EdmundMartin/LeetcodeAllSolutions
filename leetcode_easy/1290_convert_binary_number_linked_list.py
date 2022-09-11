

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next is not None:
            result = (result << 1) | head.next.val
            head = head.next
        return result