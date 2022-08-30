from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_find(tree: TreeNode, target: int, seen):
    if tree is None:
        return False
    left = recursive_find(tree.left, target, seen)
    other = target - tree.val
    if other in seen:
        return True
    seen.add(tree.val)
    return left or recursive_find(tree.right, target, seen)


# Runtime: 86 ms, faster than 91.30% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 18.1 MB, less than 68.34% of Python3 online submissions for Two Sum IV - Input is a BST.
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return recursive_find(root, k, set())