

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        iters = 0
        while n >= i:
            n = n - i
            i += 1
            iters += 1
        return iters


class SolutionBinarySearch:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            middle = (right + left) // 2
            current = middle * (middle + 1) // 2
            if current == n:
                return middle
            if n < current:
                right = middle - 1
            else:
                left = middle + 1
        return right
