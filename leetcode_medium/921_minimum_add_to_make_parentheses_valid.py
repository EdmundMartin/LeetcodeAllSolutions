

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = 0
        right_count = 0
        added = 0

        for char in s:
            if char == "(":
                left_count += 1
            else:
                if right_count < left_count:
                    right_count += 1
                else:
                    added += 1

        added += left_count - right_count
        return added


if __name__ == '__main__':
    result = Solution().minAddToMakeValid("(((")
    print(result)

    result = Solution().minAddToMakeValid("())")
    print(result)