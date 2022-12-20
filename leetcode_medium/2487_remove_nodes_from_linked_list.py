from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime beats 99.25%
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        tail = nodes[-1]
        tail_val = nodes[-1].val

        idx = len(nodes) - 2

        while idx >= 0:
            if nodes[idx].val < tail_val:
                idx -= 1
            else:
                nodes[idx].next = tail
                tail_val = nodes[idx].val
                tail = nodes[idx]
                idx -= 1
        return tail
