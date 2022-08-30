from typing import List


# Runtime: 36 ms, faster than 94.66% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14.1 MB, less than 32.50% of Python3 online submissions for Unique Number of Occurrences.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for val in arr:
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1
        return len(counter.keys()) == len(set(counter.values()))


if __name__ == '__main__':
    test_arr_one = [1, 2, 2, 1, 1, 3]

    res = Solution().uniqueOccurrences(test_arr_one)
    assert res is True

    test_arr_two = [1, 2]
    res = Solution().uniqueOccurrences(test_arr_two)
    assert res is False

    test_arr_three = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    res = Solution().uniqueOccurrences(test_arr_three)
    assert res is True