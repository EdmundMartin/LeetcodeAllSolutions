from typing import List


def find_word(board, row, col, word: str, target: str, seen):
    if word == target:
        return True
    seen.add((row, col))

    candidates = []
    for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if r >= len(board) or r < 0:
            continue
        if c >= len(board[0]) or c < 0:
            continue
        if (r, c) in seen:
            continue
        idx = len(word)
        if board[r][c] == target[idx]:
            #state = seen.copy()
            candidates.append(find_word(board, r, c, word + board[r][c], target, seen))

    if any([c is True for c in candidates]):
        return True
    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    found = find_word(board, row, col, word[0], word, set())
                    if found:
                        return True
        return False


if __name__ == '__main__':
    test_input = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    res = Solution().exist(test_input, "AAB")
    print(res)