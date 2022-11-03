from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.results = []

    def recursive(self, node: TreeNode, prior: int):
        if node is None:
            return

        prior = prior * 10
        prior = prior + node.val

        if node.left is None and node.right is None:
            self.results.append(prior)
            return

        self.recursive(node.left, prior)
        self.recursive(node.right, prior)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.recursive(root, 0)
        return sum(self.results)


if __name__ == '__main__':
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)

    result = Solution().sumNumbers(test_root)
    print(result)