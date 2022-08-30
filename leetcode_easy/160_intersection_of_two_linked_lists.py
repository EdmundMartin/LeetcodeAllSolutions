from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        current_a = headA
        while current_a:
            seen.add(current_a)
            current_a = current_a.next

        current_b = headB
        while current_b:
            if current_b in seen:
                return current_b
            current_b = current_b.next
        return current_b


class SolutionTwoPointers:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next

        return pointer_a