from typing import List


class Solution:

    def calculate_cost(self, garbage_type: str, max_idx: int, garbage: List[str], travel):
        cost = 0
        idx = 0
        while idx <= max_idx:
            cost += garbage[idx].count(garbage_type)
            if idx < max_idx:
                cost += travel[idx]
            idx += 1
        return cost

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        max_glass, max_paper, max_metal = -1, -1, -1

        for idx, g in enumerate(garbage):
            if "G" in g:
                max_glass = idx
            if "M" in g:
                max_metal = idx
            if "P" in g:
                max_paper = idx
        return self.calculate_cost("G", max_glass, garbage, travel) \
               + self.calculate_cost("P", max_paper, garbage, travel) + self.calculate_cost("M", max_metal, garbage, travel)


if __name__ == '__main__':
    res = Solution().garbageCollection(["G","P","GP","GG"], [2, 4, 3])
    print(res)