

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        idx = 0
        count = 0
        while idx < len(s) - 2:
            triplet = s[idx:idx+3]
            count += 1 if len(triplet) == len(set(triplet)) else 0
            idx += 1
        return count


if __name__ == '__main__':
    test_input = "xyzzaz"
    Solution().countGoodSubstrings(test_input)