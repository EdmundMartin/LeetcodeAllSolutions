from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node: TreeNode):
    if node is None:
        return 0, 0

    left_val, l_count = traverse(node.left)
    right_val, r_count = traverse(node.right)
    count = l_count + r_count
    if node.val == left_val + right_val:
        count += 1
    return node.val + left_val + right_val, count


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        _, count = traverse(root)
        return count


if __name__ == '__main__':
    zero_case = TreeNode(0)
    result = Solution().equalToDescendants(zero_case)
    print(result)

    test_case = TreeNode(10)
    test_case.left = TreeNode(3)
    test_case.left.left = TreeNode(2)
    test_case.left.right = TreeNode(1)
    test_case.right = TreeNode(4)

    result = Solution().equalToDescendants(test_case)
    print(result)