

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        idx = 0
        while len(friends) > 1:
            new_idx = (idx + k) - 1
            if new_idx > len(friends) - 1:
                new_idx = new_idx % len(friends)
            friends.pop(new_idx)
            idx = new_idx
        return friends[0]


if __name__ == '__main__':
    result = Solution().findTheWinner(5, 2)
    print(result)

    result = Solution().findTheWinner(6, 5)
    print(result)