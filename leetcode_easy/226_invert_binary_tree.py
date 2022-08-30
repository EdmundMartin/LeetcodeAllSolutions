from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        def dfs(node):
            left = node.left
            right = node.right

            node.right = left
            node.left = right

            if left:
                dfs(left)
            if right:
                dfs(right)
        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.right = TreeNode(12)

    Solution().invertTree(root)

    print(root.left.val)