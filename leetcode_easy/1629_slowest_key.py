from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        last_num = 0
        max_val = float('-inf')
        max_char = chr(0)
        for idx, release in enumerate(releaseTimes):
            diff = release - last_num
            if diff > max_val:
                max_char = keysPressed[idx]
                max_val = diff
            if diff == max_val:
                max_char = max_char if max_char > keysPressed[idx] else keysPressed[idx]
            last_num = release
        return max_char


if __name__ == '__main__':
    res = Solution().slowestKey([9, 29, 49, 50], "cbcd")
    print(res)
