
class Node:
    def __init__(self, val: int, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.visited = {}

    def get_cloned_node(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.get_cloned_node(old_node.random)
            new_node.next = self.get_cloned_node(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]