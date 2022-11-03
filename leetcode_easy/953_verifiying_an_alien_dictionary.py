from typing import List


def compare(order, first: str, second: str) -> bool:
    smaller = len(first) if len(first) < len(second) else len(second)

    same_chars = 0
    for idx in range(smaller):
        if order[first[idx]] < order[second[idx]]:
            return True
        elif order[first[idx]] == order[second[idx]]:
            same_chars += 1
        else:
            return False
    return len(first) <= len(second)


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        for idx, char in enumerate(order):
            ordering[char] = idx

        for idx in range(1, len(words)):
            if not compare(ordering, words[idx - 1], words[idx]):
                return False
        return True


if __name__ == '__main__':
    test_words = ["hello", "leetcode"]
    test_order = "hlabcdefgijkmnopqrstuvwxyz"

    res = Solution().isAlienSorted(test_words, test_order)
    print(res)