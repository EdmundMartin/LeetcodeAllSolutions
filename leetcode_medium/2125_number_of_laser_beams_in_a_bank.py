from typing import List


def count_row(row: str) -> int:
    return sum([1 if r == "1" else 0 for r in row])


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        last_bank = count_row(bank[0])

        for row in bank[1:]:
            current_count = count_row(row)

            if current_count == 0:
                continue
            if current_count >= 0:
                total += current_count * last_bank
                last_bank = current_count
        return total


if __name__ == '__main__':
    Solution().numberOfBeams(["011001","000000","010100","001000"])