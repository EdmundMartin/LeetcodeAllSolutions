from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)

        for idx in range(len(num)):
            if int(num[idx]) == counter[str(idx)]:
                continue
            else:
                return False
        return True
