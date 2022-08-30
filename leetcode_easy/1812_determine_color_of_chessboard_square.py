


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        column = letters.index(coordinates[0])
        row = int(coordinates[1]) - 1

        if column % 2 == 0 and row % 2 == 0:
            return False
        elif column % 2 == 0 and row % 2 != 0:
            return True
        elif column % 2 != 0 and row % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    result = Solution().squareIsWhite("a1")
    print(result)

    result = Solution().squareIsWhite("h3")
    print(result)

    result = Solution().squareIsWhite("c7")
    print(result)