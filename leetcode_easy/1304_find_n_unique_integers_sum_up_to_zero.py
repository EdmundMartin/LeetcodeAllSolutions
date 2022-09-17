from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        if n % 2 == 0:
            result = []
            for i in range(n // 2):
                i = i + 1
                result.append(-i)
                result.append(i)
            return result
        else:
            result = []
            contains = set()
            for i in range((n - 1) // 2):
                i = i + 1
                contains.add(-i)
                contains.add(i)
                result.append(-i)
                result.append(i)
            next_num = (n // 2) + 1
            negative_sum = result[-1] - next_num
            while negative_sum in contains:
                next_num += 1
                negative_sum = result[-1] - next_num
            result[-1] = negative_sum
            result.append(next_num)
            return result


if __name__ == '__main__':
    Solution().sumZero(5)