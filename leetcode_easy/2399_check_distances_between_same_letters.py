from typing import List
from string import ascii_lowercase


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = set()
        alpha = ascii_lowercase
        for idx, ch in enumerate(s):
            if ch in seen:
                continue
            offset_loc = alpha.index(ch)
            offset_size = distance[offset_loc]
            if (idx + offset_size + 1) >= len(s) or s[idx + offset_size + 1] != ch:
                return False
            seen.add(ch)
        return True


if __name__ == '__main__':
    res = Solution().checkDistances("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(res)

    res = Solution().checkDistances("aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(res)