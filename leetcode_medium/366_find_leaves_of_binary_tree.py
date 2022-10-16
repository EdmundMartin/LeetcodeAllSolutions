from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


def get_leaf_nodes(node: TreeNode, parent: Optional[TreeNode], values):
    if node is None:
        return

    if node.left is None and node.right is None:
        values.append((node, parent))
        return

    get_leaf_nodes(node.left, node, values)
    get_leaf_nodes(node.right, node, values)


def remove_nodes(node_pairs: List[Tuple[TreeNode, TreeNode]]) -> List[int]:
    result = []
    for child, parent in node_pairs:
        if parent and parent.left == child:
            parent.left = None
        if parent and parent.right == child:
            parent.right = None
        result.append(child.val)
    return result


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        has_leaves = True
        layers = []
        while has_leaves:
            values = []
            get_leaf_nodes(root, None, values)
            if len(values) == 1 and values[0][1] is None:
                has_leaves = False
            layer = remove_nodes(values)
            layers.append(layer)
        return layers


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = Solution().findLeaves(root)
    print(result)