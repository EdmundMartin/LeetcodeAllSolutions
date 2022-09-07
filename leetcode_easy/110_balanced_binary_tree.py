
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(node: TreeNode) -> [bool, int]:
    if node is None:
        return True, 0
    if node.left is None and node.right is None:
        return True, 1

    left_balanced, left_height = helper(node.left)
    right_balanced, right_height = helper(node.right)

    if abs(left_height - right_height) > 1:
        return False, max(left_height, right_height)

    if left_balanced is False or right_balanced is False:
        return False, max(left_height, right_height)
    return True, max(left_height, right_height) + 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = helper(root)
        return balanced