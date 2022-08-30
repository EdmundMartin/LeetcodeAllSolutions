from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 54 ms, faster than 70.76% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.4 MB, less than 23.19% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_depth = 1

        def dfs(node: TreeNode, depth: int):
            if depth > self.max_depth:
                self.max_depth = depth
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        dfs(root, 1)
        return self.max_depth


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.left.left = TreeNode(5)

    result = Solution().maxDepth(root)
    print(result)
