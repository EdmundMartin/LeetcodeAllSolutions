from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:

        current_m = m
        current_n = n

        prev = None
        current_node = head
        while current_node:
            if current_m > 0:
                prev = current_node
                current_node = current_node.next
                current_m -= 1
                continue
            if current_n == 0:
                current_m = m
                current_n = n
            else:
                prev.next = current_node.next
                current_node = current_node.next
                current_n -= 1
        return head


def build_from_array(nums: List[int]):
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def to_list(head: ListNode) -> List[int]:
    current = head
    vals = []
    while current:
        vals.append(current.val)
        current = current.next
    return vals


if __name__ == '__main__':
    test_array = build_from_array([1,2,3,4,5,6,7,8,9,10,11])
    result = Solution().deleteNodes(test_array, 1, 3)

    print(to_list(result))

    test_array = build_from_array([1,2,3,4,5,6,7,8,9,10,11,12,13])
    result = Solution().deleteNodes(test_array, 2, 3)
    print(to_list(result))