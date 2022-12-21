from typing import List


def two_edits_away(candidate: str, dictionary_word: str):
    count = 0
    idx = 0
    while idx < len(dictionary_word):
        if candidate[idx] != dictionary_word[idx]:
            count += 1
        if count > 2:
            return False
        idx += 1
    return count <= 2


# Beats 97.95 on runtime
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        output = []
        for query in queries:
            solved = False
            for dict_word in dictionary:
                if solved:
                    continue
                if two_edits_away(query, dict_word):
                    output.append(query)
                    solved = True
        return output


if __name__ == '__main__':
    q = ["t","i","m","i","p","s"]
    d = ["w","j","b","p","u","b","u","i","h","m"]
    res = Solution().twoEditWords(q, d)
    print(res)