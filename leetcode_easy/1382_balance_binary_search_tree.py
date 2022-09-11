from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_tree(nums: List[int], left, right) -> Optional[TreeNode]:
    if left > right:
        return

    middle = (left + right) // 2

    root = TreeNode(nums[middle])
    root.left = balance_tree(nums, left, middle - 1)
    root.right = balance_tree(nums, middle + 1, right)
    return root


def in_order(root, values):
    if root is None:
        return
    in_order(root.left, values)
    values.append(root.val)
    in_order(root.right, values)


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        in_order(root, values)
        return balance_tree(values, 0, len(values) - 1)