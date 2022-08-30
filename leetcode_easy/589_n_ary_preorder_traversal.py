from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def pre_order(self, root: Node, values: List[int]):
        values.append(root.val)
        if root.children:
            for child in root.children:
                self.pre_order(child, values)

    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        values = []
        self.pre_order(root, values)
        return values


if __name__ == '__main__':
    tree = Node(1)
    tree.children = [Node(3), Node(2), Node(4)]
    tree.children[0].children = [Node(5), Node(6)]

    result = Solution().preorder(tree)
    print(result)