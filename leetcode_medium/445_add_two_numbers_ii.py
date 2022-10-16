from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_stack(head: ListNode):
    stack = []
    current = head
    while current:
        stack.append(current.val)
        current = current.next
    return stack


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = to_stack(l1), to_stack(l2)

        remainder = 0
        head = None
        while first or second:
            num_one = first.pop() if first else 0
            num_two = second.pop() if second else 0
            current_num = (num_one + num_two + remainder) % 10
            remainder = (num_one + num_two + remainder) // 10
            node = ListNode(current_num)
            node.next = head
            head = node
        if remainder:
            node = ListNode(remainder)
            node.next = head
            head = node
        return head


def iterate(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == '__main__':
    first = ListNode(7)
    first.next = ListNode(2)
    first.next.next = ListNode(4)
    first.next.next.next = ListNode(3)

    second = ListNode(5)
    second.next = ListNode(6)
    second.next.next = ListNode(4)

    result = Solution().addTwoNumbers(first, second)
    print(iterate(result))


    first = ListNode(2)
    first.next = ListNode(4)
    first.next.next = ListNode(3)

    second = ListNode(5)
    second.next = ListNode(6)
    second.next.next = ListNode(4)

    result = Solution().addTwoNumbers(first, second)
    print(iterate(result))

    first = ListNode(9)
    second = ListNode(9)
    result = Solution().addTwoNumbers(first, second)
    print(iterate(result))