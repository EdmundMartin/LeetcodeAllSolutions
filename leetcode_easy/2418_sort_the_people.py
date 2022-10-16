from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        all_people = [(names[i], heights[i]) for i in range(len(names))]
        return [i[0] for i in sorted(all_people, key=lambda x: x[1], reverse=True)]