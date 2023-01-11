from typing import List


def split_num(num: int) -> List[int]:
    result = []
    while num >= 10:
        remainder = num % 10
        num = num // 10
        result.append(remainder)
    result.append(num)
    return result


class Solution:
    def countDigits(self, num: int) -> int:
        digits = split_num(num)
        count: int = 0
        for dig in digits:
            if num % dig == 0:
                count += 1
        return count


if __name__ == '__main__':
    print(split_num(121))