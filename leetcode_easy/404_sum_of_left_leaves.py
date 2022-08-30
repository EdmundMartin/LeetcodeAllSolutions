from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursive_solution(self, node: Optional[TreeNode], parent_relation: Optional[str]):
        if node is None:
            return
        if parent_relation and parent_relation == "LEFT":
            if node.left is None and node.right is None:
                self.sum += node.val
        self.recursive_solution(node.left, "LEFT")
        self.recursive_solution(node.right, "RIGHT")

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.recursive_solution(root, None)
        return self.sum


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().sumOfLeftLeaves(root)
    print(result)