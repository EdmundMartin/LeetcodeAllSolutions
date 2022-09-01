from typing import List
from string import ascii_lowercase


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count = 1
        current_page = 100
        for char in s:
            current_width = widths[ascii_lowercase.index(char)]
            if current_width > current_page:
                count += 1
                current_page = 100
            current_page -= current_width
        return [count, 100 - current_page]

