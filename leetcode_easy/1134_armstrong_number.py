

def calculate_armstrong(number: int, target: int) -> bool:
    result = []
    while number >= 10:
        result.append(number % 10)
        number //= 10
    result.append(number)
    n = len(result)
    total = 0
    for r in result:
        total += r ** n
    return total == target


class Solution:
    def isArmstrong(self, n: int) -> bool:
        return calculate_armstrong(n, n)


if __name__ == '__main__':
    calculate_armstrong(153, 153)