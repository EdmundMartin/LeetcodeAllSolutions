

# Runtime: 39 ms, faster than 94.75% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
# Memory Usage: 14.9 MB, less than 96.72% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
class Solution:

    def get_right_boundary(self, reader: 'ArrayReader', target: int) -> int:
        right = 1
        while reader.get(right) < target:
            right <<= 1
        return right

    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = self.get_right_boundary(reader, target)
        while left <= right:
            middle = (left + right) // 2
            current = reader.get(middle)
            if current == target:
                return middle
            elif current > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
