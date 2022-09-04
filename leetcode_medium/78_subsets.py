from typing import List, Set


def generate_subsets(values: List[int], seen: Set):
    if len(values) == 0:
        seen.add(())
        return
    seen.add(tuple(values))
    for idx in range(len(values)):
        generate_subsets(values[:idx] + values[idx + 1:], seen)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        generate_subsets(nums, seen)
        return [list(t) for t in seen]


if __name__ == '__main__':
    results = set()
    generate_subsets([1, 2, 3], results)
    print(results)