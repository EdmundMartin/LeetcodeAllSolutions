from string import ascii_lowercase


# Runtime: 33 ms, faster than 91.62% of Python3 online submissions for Replace All Digits with Characters.
# Memory Usage: 13.8 MB, less than 58.54% of Python3 online submissions for Replace All Digits with Characters.
class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = list(s)
        idx = 0
        while idx + 1 < len(arr):
            letter = arr[idx]
            shift = arr[idx + 1]
            arr[idx + 1] = ascii_lowercase[ascii_lowercase.index(letter) + int(shift)]
            idx += 2
        return "".join(arr)


if __name__ == '__main__':
    test_one = "a1c1e1"
    res = Solution().replaceDigits(test_one)
    print(res)

    test_two = "a1b2c3d4e"
    res = Solution().replaceDigits(test_two)
    print(res)