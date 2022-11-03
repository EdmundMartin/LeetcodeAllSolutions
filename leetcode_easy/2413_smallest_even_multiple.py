

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        start_num = n if n % 2 == 0 else n + 1
        while start_num % n != 0 or start_num % 2 != 0:
            start_num += 2
        return start_num