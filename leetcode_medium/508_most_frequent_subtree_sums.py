from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node: TreeNode, counter):
    if node is None:
        return 0
    left_sum = traverse(node.left, counter)
    right_sum = traverse(node.right, counter)
    total = left_sum + right_sum + node.val
    if total in counter:
        counter[total] += 1
    else:
        counter[total] = 1
    return total


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = dict()
        traverse(root, counter)
        most_frequent = max(counter.values())
        return [k for k, v in counter.items() if v == most_frequent]


if __name__ == '__main__':
    root_node = TreeNode(5)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(-5)

    Solution().findFrequentTreeSum(root_node)