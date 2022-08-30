# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

GLOBAL_VALUE = 6


def guess(num: int) -> int:
    if num == GLOBAL_VALUE:
        return 0
    if num < GLOBAL_VALUE:
        return 1
    else:
        return -1


# Runtime: 32 ms, faster than 91.30% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 13.9 MB, less than 66.35% of Python3 online submissions for Guess Number Higher or Lower.
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            guess_result = guess(middle)
            if guess_result == 0:
                return middle
            elif guess_result > 0:
                left = middle + 1
            else:
                right = middle - 1


if __name__ == '__main__':
    result = Solution().guessNumber(10)
    print(result)