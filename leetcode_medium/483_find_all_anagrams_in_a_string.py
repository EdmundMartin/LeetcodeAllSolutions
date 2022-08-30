from typing import List
from collections import Counter


class SolutionToSlow:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        found = []
        counts = Counter(p)
        idx = 0
        while idx < len(s):
            second = idx
            counter = counts.copy()
            while second <= idx + len(p) and second < len(s):
                if s[second] not in counter:
                    break
                elif counter[s[second]] <= 0:
                    break
                else:
                    counter[s[second]] -= 1
                    second += 1
            if second == idx + len(p):
                found.append(idx)
            idx += 1
        return found


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size_s, size_p = len(s), len(p)
        if size_s < size_p:
            return []
        p_count = Counter(p)
        s_count = Counter()

        output = []
        for i in range(size_s):
            s_count[s[i]] += 1

            if i >= size_p:
                if s_count[s[i - size_p]] == 1:
                    del s_count[s[i - size_p]]
                else:
                    s_count[s[i - size_p]] -= 1

            if p_count == s_count:
                output.append(i - size_p + 1)
        return output


if __name__ == '__main__':
    test_s = "cbaebabacd"
    test_p = "abc"

    res = SolutionToSlow().findAnagrams(test_s, test_p)
    print(res)