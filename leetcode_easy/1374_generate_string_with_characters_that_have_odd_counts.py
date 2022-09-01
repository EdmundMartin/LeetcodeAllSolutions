

class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        if n % 2 == 0:
            result = ('a' * (n - 1)) + 'b'
        else:
            result = 'a' + ('b' * (n - 2)) + 'c'
        return result


if __name__ == '__main__':
    result = Solution().generateTheString(7)
    print(result)