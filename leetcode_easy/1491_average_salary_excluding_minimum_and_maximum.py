from typing import List


class MinMaxTracker:
    def __init__(self):
        self.total = 0
        self.count = 0
        self.min = float('inf')
        self.max = float('-inf')

    def set_value(self, val: int):
        self.total += val
        self.count += 1
        if val < self.min:
            self.min = val
        if val > self.max:
            self.max = val

    def average(self):
        return (self.total - (self.min + self.max)) / (self.count - 2)


class Solution:
    def average(self, salary: List[int]) -> float:
        tracker = MinMaxTracker()
        for num in salary:
            tracker.set_value(num)
        return tracker.average()


# Runtime: 35 ms, faster than 88.21% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.9 MB, less than 54.37% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
class SolutionAlt:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        return sum(salary[1:-1]) / len(salary[1:-1])


if __name__ == '__main__':
    salary = [4000, 3000, 1000, 2000]
    result = SolutionAlt().average(salary)
    print(result)