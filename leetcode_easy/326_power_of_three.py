
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == '__main__':
    res = Solution().isPowerOfThree(45)
    print(res)

    res = Solution().isPowerOfThree(27)
    print(res)