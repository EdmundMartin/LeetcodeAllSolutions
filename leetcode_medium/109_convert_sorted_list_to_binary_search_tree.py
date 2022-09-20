from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced_bst(arr: List[int], left, right) -> Optional[TreeNode]:
    if left > right:
        return None

    middle = (left + right) // 2

    root = TreeNode(arr[middle])
    root.left = balanced_bst(arr, left, middle - 1)
    root.right = balanced_bst(arr, middle + 1, right)
    return root


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sorted_nums = []
        while head:
            sorted_nums.append(head.val)
            head = head.next
        if len(sorted_nums) == 0:
            return
        return balanced_bst(sorted_nums, 0, len(sorted_nums) - 1)