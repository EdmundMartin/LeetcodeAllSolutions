from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order(node: TreeNode, values: List[int]):
    if node is None:
        return
    in_order(node.left, values)
    values.append(node.val)
    in_order(node.right, values)


class SolutionNaive:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = []
        in_order(root1, values)
        in_order(root2, values)
        return sorted(values)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = []
        stack_one, stack_two = [], []

        while root1 or root2 or stack_one or stack_two:

            while root1:
                stack_one.append(root1)
                root1 = root1.left
            while root2:
                stack_two.append(root2)
                root2 = root2.left

            if not stack_two or stack_one and stack_one[-1].val <= stack_two[-1].val:
                root1 = stack_one.pop()
                values.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack_two.pop()
                values.append(root2.val)
                root2 = root2.right
        return values