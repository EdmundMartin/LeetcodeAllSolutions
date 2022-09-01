from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter_one = {}
        counter_two = {}

        for w in words1:
            if w not in counter_one:
                counter_one[w] = 0
            counter_one[w] += 1
        for w in words2:
            if w not in counter_two:
                counter_two[w] = 0
            counter_two[w] += 1

        count = 0
        for result, items in counter_one.items():
            if items == 1 and result in counter_two and counter_two[result] == 1:
                count += 1

        return count


if __name__ == '__main__':
    test_one = ["a", "ab"]
    test_two = ["a"]