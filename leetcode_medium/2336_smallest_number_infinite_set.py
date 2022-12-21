

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest: int = 1
        self.removed = set()

    def popSmallest(self) -> int:
        ret_val = self.smallest
        next_value = ret_val + 1
        if next_value not in self.removed:
            self.smallest = next_value
            self.removed.add(ret_val)
            return ret_val
        while next_value in self.removed:
            next_value += 1
        self.smallest = next_value
        self.removed.add(ret_val)
        return ret_val

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        if num < self.smallest:
            self.smallest = num
        return


if __name__ == '__main__':
    res = SmallestInfiniteSet()

    res.popSmallest()
    res.popSmallest()
    res.popSmallest()

    res.addBack(1)
    print(res.popSmallest())
    print(res.popSmallest())