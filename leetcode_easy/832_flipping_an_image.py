from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for r in range(len(image)):
            row = image[r]
            row = row[::-1]
            row = [1 if r == 0 else 0 for r in row]
            image[r] = row
        return image