from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []

        current = defaultdict(list)
        for idx, size in enumerate(groupSizes):
            current[size].append(idx)

        temp_result = []
        for key, value in current.items():
            temp_result.append((key, value))

        temp_result = sorted(temp_result, key=lambda x: x[0])
        for item in temp_result:
            size, idxs = item
            if len(idxs) > size:
                while len(idxs) > 0:
                    result.append(idxs[:size])
                    idxs = idxs[size:]
            else:
                result.append(idxs)
        return result

if __name__ == '__main__':
    Solution().groupThePeople([3,3,3,3,3,1,3])