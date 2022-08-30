from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_arr = [None] * len(s)

        for idx, char in enumerate(s):
            new_arr[indices[idx]] = char
        return ''.join(new_arr)


if __name__ == '__main__':
    result = Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
    print(result)