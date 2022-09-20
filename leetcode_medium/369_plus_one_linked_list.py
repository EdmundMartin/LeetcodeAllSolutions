

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        carry = 0
        while stack:
            curr_nod = stack.pop()
            curr_nod.val += 1
            if curr_nod.val > 9:
                curr_nod.val = 0
                carry = 1
            else:
                carry = 0
            if carry == 0:
                break
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        return head