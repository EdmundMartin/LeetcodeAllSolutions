from string import digits


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""

        pointer_one = len(num1) - 1
        pointer_two = len(num2) - 1

        carry = 0
        while pointer_one >= 0 or pointer_two >= 0:
            first_digit = 0 if pointer_one < 0 else digits.index(num1[pointer_one]) - digits.index("0")
            second_digit = 0 if pointer_two < 0 else digits.index(num2[pointer_two]) - digits.index("0")

            value = (first_digit + second_digit + carry) % 10
            carry = (first_digit + second_digit + carry) // 10
            result += str(value)

            pointer_one -= 1
            pointer_two -= 1

        if carry > 0:
            result += str(carry)
        return result[::-1]


if __name__ == '__main__':
    result = Solution().addStrings("123", "23")
    print(result)