from typing import Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def remove(self, key: int):
        if self.head is None:
            return
        if self.head.key == key:
            if self.head == self.tail:
                self.tail = None
                self.head = None
                return
            self.head = self.head.next
            return
        current_node = self.head
        while current_node:
            if current_node.key == key:
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                return
        return

    def search(self, key: int) -> bool:
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return True
            current_node = current_node.next
        return False

    def add(self, key: int):
        if self.search(key):
            return
        if self.head is None:
            node = Node(key)
            self.head = node
            self.tail = node
            return
        new_head = Node(key)
        new_head.next = self.head
        self.head = new_head

    def __repr__(self):
        results = []
        current = self.head
        while current:
            results.append(current.key)
            current = current.next
        return str(results)


# Runtime: 271 ms, faster than 67.17% of Python3 online submissions for Design HashSet.
# Memory Usage: 22.6 MB, less than 16.22% of Python3 online submissions for Design HashSet.
class MyHashSet:

    def __init__(self):
        self.mod = 3
        self.buckets = [None] * self.mod

    def add(self, key: int) -> None:
        bucket_id = hash(key) % self.mod
        if self.buckets[bucket_id] is None:
            ll = LinkedList()
            ll.add(key)
            self.buckets[bucket_id] = ll
        else:
            self.buckets[bucket_id].add(key)

    def remove(self, key: int) -> None:
        bucket_id = hash(key) % self.mod
        if self.buckets[bucket_id] is None:
            return
        self.buckets[bucket_id].remove(key)

    def contains(self, key: int) -> bool:
        bucket_id = hash(key) % self.mod
        if self.buckets[bucket_id] is None:
            return False
        return self.buckets[bucket_id].search(key)


if __name__ == '__main__':
    test = MyHashSet()
    test.add(10)
    test.add(17)
    test.add(12)
    test.add(123)
    print(test.buckets)
    test.remove(123)
    print(test.buckets)
    res = test.contains(123)
    print(res)
    print(test.buckets)
    test.remove(12)
    print(test.buckets)
    test.add(12)
    print(test.buckets)
    print(test.contains(17))