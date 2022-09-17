

class TwoSum:

    def __init__(self):
        self.values = []
        self.sorted = False

    def add(self, number: int) -> None:
        self.values.append(number)
        self.sorted = False

    def find(self, value: int) -> bool:
        if not self.sorted:
            self.values.sort()
            self.sorted = True

        left = 0
        right = len(self.values) - 1

        while left < right:
            current_sum = self.values[left] + self.values[right]
            if current_sum > value:
                right -= 1
            elif current_sum < value:
                left += 1
            else:
                return True
        return False