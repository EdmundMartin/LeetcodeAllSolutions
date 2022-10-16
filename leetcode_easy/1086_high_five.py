from typing import List
import heapq
from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        students = defaultdict(list)

        for item in items:
            students[item[0]].append(item[1])

        output = []
        for student, results in students.items():
            heapq.heapify(results)
            output.append(
                [student, sum([r for r in heapq.nlargest(5, results)])//5]
            )
        output.sort(key=lambda x: x[0])
        return output