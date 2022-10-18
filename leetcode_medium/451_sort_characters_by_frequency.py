from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        result = defaultdict(int)
        for char in s:
            result[char] += 1
        pairs = list(result.items())
        pairs.sort(key=lambda x: x[1])
        result_str = ""
        while pairs:
            ch, val = pairs.pop()
            result_str += ch * val
        return result_str


if __name__ == '__main__':
    res = Solution().frequencySort("tree")
    print(res)