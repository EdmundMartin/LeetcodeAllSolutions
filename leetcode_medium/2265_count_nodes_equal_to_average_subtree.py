from typing import Optional


class SubTree:
    def __init__(self, total=0, count=0):
        self.total = total
        self.count = count

    def add(self, val: int):
        self.total += val
        self.count += 1

    def average(self):
        return self.total // self.count

    def __add__(self, other):
        return SubTree(total=self.total+other.total, count=self.count+other.count)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node: TreeNode):
    if node is None:
        return SubTree(), 0

    left_tree, l_count = traverse(node.left)
    right_tree, r_count = traverse(node.right)

    current_count = l_count + r_count
    current_subtree = left_tree + right_tree + SubTree(node.val, 1)
    if current_subtree.average() == node.val:
        current_count += 1
    return current_subtree, current_count


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _, count = traverse(root)
        return count