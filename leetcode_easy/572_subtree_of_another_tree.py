from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(left: TreeNode, right: TreeNode) -> bool:
    if left is None and right is None:
        return True
    if left is None and right:
        return False
    if right is None and left:
        return False
    if left.val != right.val:
        return False
    left_is_same = is_same_tree(left.left, right.left)
    return left_is_same and is_same_tree(left.right, right.right)


def traverse_roots(root: TreeNode, sub_tree: TreeNode, roots: List[TreeNode]):
    if root is None:
        return
    if root.val == sub_tree.val:
        roots.append(root)
    traverse_roots(root.left, sub_tree, roots)
    traverse_roots(root.right, sub_tree, roots)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        roots = []
        traverse_roots(root, subRoot, roots)
        for candidate in roots:
            result = is_same_tree(candidate, subRoot)
            if result is True:
                return result
        return False


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    sub_root = root.left

    res = Solution().isSubtree(root, sub_root)
    print(res)