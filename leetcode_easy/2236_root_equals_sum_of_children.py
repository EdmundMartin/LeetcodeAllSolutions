from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.left)
        self.total += root.val
        self.traverse(root.right)

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        self.total = 0
        self.traverse(root)
        return self.total - root.val == root.val


if __name__ == '__main__':
    r = TreeNode(10)
    r.left = TreeNode(4)
    r.right = TreeNode(6)

    result = Solution().checkTree(r)
    print(result)