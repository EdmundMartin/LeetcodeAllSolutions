from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cites = set()
        end_cites = set()

        for path in paths:
            start_cites.add(path[0])
            end_cites.add(path[1])
        return end_cites.difference(start_cites).pop()


if __name__ == '__main__':
    test_paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    result = Solution().destCity(test_paths)
    print(result)

    test_paths = [["B","C"],["D","B"],["C","A"]]
    result = Solution().destCity(test_paths)
    print(result)