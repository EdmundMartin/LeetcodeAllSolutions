from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


# Runtime: 23 ms, faster than 99.96% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 79.86% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None and list2:
            return list2
        if list2 is None and list1:
            return list1

        if list1.val < list2.val:
            node = list1
            head = prev = node
            list1 = list1.next
        else:
            node = list2
            head = prev = node
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2

        return head


