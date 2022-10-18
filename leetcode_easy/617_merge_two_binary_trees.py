from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solution(left_tree: TreeNode, right_tree: TreeNode):
    if left_tree is None and right_tree is None:
        return

    new_node = TreeNode()

    if left_tree and right_tree:
        new_node.val = left_tree.val + right_tree.val
    elif left_tree:
        new_node.val = left_tree.val
    elif right_tree:
        new_node.val = right_tree.val

    left_tree_l = left_tree.left if left_tree else None
    right_tree_l = right_tree.left if right_tree else None
    new_node.left = recursive_solution(left_tree_l, right_tree_l)

    left_tree_r = left_tree.right if left_tree else None
    right_tree_r = right_tree.right if right_tree else None
    new_node.right = recursive_solution(left_tree_r, right_tree_r)

    return new_node


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return recursive_solution(root1, root2)