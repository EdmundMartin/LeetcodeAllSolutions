from typing import List


def search(image, sr, sc: int, color: int, target_color: int):
    stack = [(sr, sc)]
    seen = set()
    seen.add((sr, sc))
    while stack:
        x, y = stack.pop()
        seen.add((x, y))
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
            continue
        if image[x][y] == color:
            image[x][y] = target_color
            for cord in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if cord not in seen:
                    seen.add(cord)
                    stack.append(cord)
        else:
            seen.add((x, y))


# Runtime: 82 ms, faster than 89.67% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 66.14% of Python3 online submissions for Flood Fill.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        search(image, sr, sc, starting_color, color)
        return image