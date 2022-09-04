

def groups(s: str, k: int):
    new_chars = []
    while len(s) > k:
        words = s[:k]
        s = s[k:]
        new_chars += str(sum([int(i) for i in words]))
    if len(s) > 0:
        new_chars += str(sum([int(i) for i in s]))
    return ''.join(new_chars)


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = groups(s, k)
        return s


if __name__ == '__main__':
    res = Solution().digitSum("11111222223", 3)
    print(res)
