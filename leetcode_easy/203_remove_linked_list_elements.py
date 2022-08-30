from typing import Optional, List


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head

        prev = None
        while current_node:
            if current_node.val == val and not prev:
                head = current_node.next
                current_node = current_node.next
                continue
            elif current_node.val == val and prev:
                prev.next = current_node.next
                current_node = current_node.next
            else:
                prev = current_node
                current_node = current_node.next
        return head


def create_linked_list(vals: List) -> ListNode:
    head = ListNode(vals[0])
    current_node = head
    for val in vals[1:]:
        current_node.next = ListNode(val)
        current_node = current_node.next
    return head


def print_linked_list(head: ListNode):
    vals = []
    current_node = head
    while current_node:
        vals.append(current_node.val)
        current_node = current_node.next
    print(vals)


if __name__ == '__main__':
    result = create_linked_list([1, 2, 6, 3, 4, 5, 6])

    list_one = Solution().removeElements(result, 6)
    print_linked_list(list_one)

    empty = Solution().removeElements(None, 1)
    print(empty)

    all_sevens = Solution().removeElements(create_linked_list([7, 7, 7, 7]), 7)
    print(all_sevens)