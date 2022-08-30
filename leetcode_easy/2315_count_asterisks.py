from typing import List


class Solution:
    def countAsterisks(self, s: str) -> int:
        seen_bar = False
        count = 0
        for ch in s:
            if ch == "|":
                seen_bar = not seen_bar
            elif ch == "*" and not seen_bar:
                count += 1
        return count


if __name__ == '__main__':
    test_input = "l|*e*et|c**o|*de|"

    Solution().countAsterisks(test_input)

    test_input = "|**|*|*|**||***||"
    Solution().countAsterisks(test_input)