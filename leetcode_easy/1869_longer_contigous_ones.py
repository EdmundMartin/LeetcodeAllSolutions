

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest = (-1, "")
        prev = None
        current_count = 0
        for char in s:
            if char == prev:
                current_count += 1
            else:
                current_count = 1
            if current_count >= longest[0]:
                if current_count == longest[0] and char == "0":
                    longest = (current_count, char)
                elif current_count > longest[0]:
                    longest = (current_count, char)
            prev = char
        return longest[1] == "1"


if __name__ == '__main__':
    res = Solution().checkZeroOnes("1101")
    print(res)

    res = Solution().checkZeroOnes("111000")
    print(res)

    res = Solution().checkZeroOnes("110100010")
    print(res)