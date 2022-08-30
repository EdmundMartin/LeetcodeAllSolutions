
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node'):
        if not root:
            return

        node_copy = Node(root.val)

        for child in root.children:
            node_copy.children.append(self.cloneTree(child))

        return node_copy


if __name__ == '__main__':
    root = Node(1)
    print(root)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]


    result = Solution().cloneTree(root)
    print(result)