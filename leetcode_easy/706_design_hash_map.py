
class StorageContainer:

    def __init__(self):
        self.container = [None] * 100

    def contains(self, key: int):
        hash_key = hash(key) % len(self.container)
        return self.container[hash_key] is not None

    def set(self, key: int, value: int):
        hash_key = hash(key) % len(self.container)
        self.container[hash_key] = value

    def remove(self, key):
        hash_key = hash(key) % len(self.container)
        self.container[hash_key] = None

    def get(self, key):
        hash_key = hash(key) % len(self.container)
        if not self.contains(key):
            return -1
        return self.container[hash_key]


class MyHashMap:

    def __init__(self):
        self._storage = [None] * 100_000

    def put(self, key: int, value: int) -> None:
        key_hash = hash(key) % len(self._storage)
        store = self._storage[key_hash]
        if store is None:
            self._storage[key_hash] = StorageContainer()
            self._storage[key_hash].set(key, value)
        self._storage[key_hash].set(key, value)

    def get(self, key: int) -> int:
        key_hash = hash(key) % len(self._storage)
        store = self._storage[key_hash]
        if store is None:
            return -1
        result = store.get(key)
        if result is None:
            return -1
        return result

    def remove(self, key: int) -> None:
        key_hash = hash(key) % len(self._storage)
        store = self._storage[key_hash]
        if store is None:
            return
        store.remove(key)


if __name__ == '__main__':
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    result = hashmap.get(1)
    print(result)

    result = hashmap.get(3)
    print(result)

    hashmap.put(2, 1)
    result = hashmap.get(2)
    print(result)

    hashmap.remove(2)
    result = hashmap.get(2)
    print(result)