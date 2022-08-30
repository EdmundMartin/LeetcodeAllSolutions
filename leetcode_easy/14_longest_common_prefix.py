from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_idx = min(len(i) for i in strs)
        common_prefix = ""
        for idx in range(max_idx):
            same_prefix = set(f[idx] for f in strs)
            if len(same_prefix) == 1:
                common_prefix += strs[0][idx]
            else:
                return common_prefix
        return common_prefix


if __name__ == '__main__':
    test_one = ["flower", "flow", "flight"]
    result = Solution().longestCommonPrefix(test_one)
    print(result)

    test_two = ["dog", "racecar", "car"]
    result = Solution().longestCommonPrefix(test_two)
    print(result)