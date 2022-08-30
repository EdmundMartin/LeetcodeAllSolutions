from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx_one, idx_two = -1, -1
        min_distance = len(wordsDict)

        for idx, word in enumerate(wordsDict):
            if word == word1:
                idx_one = idx
            elif word == word2:
                idx_two = idx

            if idx_one != -1 and idx_two != -1:
                min_distance = min(min_distance, abs(idx_two - idx_one))
        return min_distance



if __name__ == '__main__':
    word_dict = ["practice", "makes", "perfect", "coding", "makes"]
    word_one = "coding"
    word_two = "practice"

    result = Solution().shortestDistance(word_dict, word_one, word_two)
    print(result)

    word_dict = ["a", "c", "b", "b", "a"]
    result = Solution().shortestDistance(word_dict, "a", "b")
    print(result)