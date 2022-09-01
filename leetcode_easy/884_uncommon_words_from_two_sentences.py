from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = {}
        for idx, sent in enumerate([s1, s2]):
            for word in sent.split(" "):
                if word not in counter:
                    counter[word] = ""
                counter[word] += str(idx)
        return [k for k, v in counter.items() if len(v) == 1]