

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_in_order(node: TreeNode, values):
    if node is None:
        return
    recursive_in_order(node.left, values)
    values.append(node.val)
    recursive_in_order(node.right, values)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        recursive_in_order(root, values)
        head = TreeNode(0)
        current = head
        for val in values:
            current.right = TreeNode(val)
            current = current.right
        return head.right