from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * (n + 1)
        self.idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:

        self.values[idKey - 1] = value
        result = []

        while self.values[self.idx] is not None:
            result.append(self.values[self.idx])
            self.idx += 1
        return result
