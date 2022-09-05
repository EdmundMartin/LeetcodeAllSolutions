from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = [i for i in range(N)]

        ans = [None] * N
        for card in sorted(deck):
            ans[index.pop(0)] = card
            if index:
                index.append(index.pop(0))
        return ans


if __name__ == '__main__':
    test_deck = [17, 13, 11, 2, 3, 5, 7]
    result = Solution().deckRevealedIncreasing(test_deck)
    print(result)