from typing import List


# Runtime: 41 ms, faster than 95.80% of Python3 online submissions for Maximum Number of Words Found in Sentences.
# Memory Usage: 14 MB, less than 6.97% of Python3 online submissions for Maximum Number of Words Found in Sentences.
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split(' ')) for s in sentences])