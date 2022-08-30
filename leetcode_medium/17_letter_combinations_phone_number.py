from typing import List

PHONE_MAPPING = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def solve_recursive(prefix: str, numbers: str, values: List[str]) -> None:
    if len(numbers) == 0:
        values.append(prefix)
        return
    opts = PHONE_MAPPING[numbers[0]]
    for opt in opts:
        solve_recursive(prefix + opt, numbers[1:], values)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        values = []
        solve_recursive("", digits, values)
        return values


if __name__ == '__main__':
    result = Solution().letterCombinations("23")
    print(result)