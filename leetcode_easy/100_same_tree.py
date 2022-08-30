from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = [(p, q)]

        while queue:
            first_node, second_node = queue.pop(0)

            if first_node is None and second_node is not None:
                return False
            if second_node is None and first_node is not None:
                return False

            if first_node is None and second_node is None:
                continue

            if first_node.val != second_node.val:
                return False

            queue.append((first_node.left, second_node.left))
            queue.append((first_node.right, second_node.right))
        return True


if __name__ == '__main__':
    first = TreeNode(1)
    first.left = TreeNode(2)
    first.right = TreeNode(3)

    second = TreeNode(1)
    second.left = TreeNode(2)
    second.right = TreeNode(3)

    result = Solution().isSameTree(first, second)
    print(result)