

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten_dfs(prev: 'Node', current: 'Node'):
    if current is None:
        return prev
    current.prev = prev
    prev.next = current

    temp_next = current.next
    tail = flatten_dfs(current, current.child)
    current.child = None
    return flatten_dfs(tail, temp_next)


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        dummy = Node(0, None, head, None)
        flatten_dfs(dummy, head)

        dummy.next.prev = None
        return dummy.next