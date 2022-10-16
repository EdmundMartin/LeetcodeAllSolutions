from random import choice


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.hash_map:
            return False
        last_element, idx = self.values[-1], self.hash_map[val]

        self.values[idx], self.hash_map[last_element] = last_element, idx
        self.values.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values)