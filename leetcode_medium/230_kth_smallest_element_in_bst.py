from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root: TreeNode, values: List[int], k):
    if root is None:
        return
    if len(values) == k:
        return
    traverse(root.left, values, k)
    if len(values) == k:
        return
    values.append(root.val)
    if len(values) == k:
        return
    traverse(root.right, values, k)


# Runtime: 47 ms, faster than 98.43% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 88.87% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        traverse(root, values, k)
        return values[-1]


if __name__ == '__main__':
    root_node = TreeNode(3)
    root_node.left = TreeNode(1)
    root_node.right = TreeNode(4)
    root_node.left.right = TreeNode(2)

    res = Solution().kthSmallest(root_node, 1)
    print(res)