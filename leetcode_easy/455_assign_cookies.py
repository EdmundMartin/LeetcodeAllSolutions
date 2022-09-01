from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        while g and s:
            if g[-1] <= s[-1]:
                count += 1
                g = g[:-1]
                s = s[:-1]
            else:
                g = g[:-1]
        return count


if __name__ == '__main__':
    result = Solution().findContentChildren([1, 2, 3], [1, 1])
    print(result)

    result = Solution().findContentChildren([1, 2], [1, 2, 3])
    print(result)