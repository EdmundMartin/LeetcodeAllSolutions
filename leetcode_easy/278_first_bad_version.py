
VERSION = 75

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    global VERSION
    return version >= VERSION


def lowest_binary_search(n: int) -> int:
    left = 1
    right = n
    first_bad_version = float('inf')
    while left <= right:

        middle = (left + right) // 2
        if isBadVersion(middle):
            first_bad_version = min(first_bad_version, middle)
            right = middle - 1
        else:
            left = middle + 1
    return first_bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return lowest_binary_search(n)


if __name__ == '__main__':
    result = Solution().firstBadVersion(255)
    print(result)