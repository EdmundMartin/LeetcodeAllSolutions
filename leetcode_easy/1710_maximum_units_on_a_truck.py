from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_types = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        unit_count = 0
        for box_type in box_types:
            box_count = min(truckSize, box_type[0])
            unit_count += box_count * box_type[1]
            truckSize -= box_count
            if truckSize == 0:
                break
        return unit_count



if __name__ == '__main__':
    result = Solution().maximumUnits([[1,3],[2,2],[3,1]], 4)
    print(result)

