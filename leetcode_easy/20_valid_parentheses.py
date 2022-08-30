

class Solution:
    def isValid(self, s: str) -> bool:
        starts = {"(", "[", "{"}
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for val in s:
            if val in starts:
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if mapping[val] != top:
                    return False
                stack = stack[:-1]
        return len(stack) == 0


if __name__ == '__main__':
    test_one = "()"

    res = Solution().isValid(test_one)
    assert res is True

    test_two = "()[]{}"
    res = Solution().isValid(test_two)
    assert res is True

    test_three = "(]"
    res = Solution().isValid(test_three)
    assert res is False