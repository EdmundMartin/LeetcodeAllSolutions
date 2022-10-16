


class SolutionBruteForce:
    def removeDuplicates(self, s: str, k: int) -> str:
        length = -1

        while length != len(s):
            length = len(s)
            idx = 0
            count = 0
            while idx < len(s):
                if idx == 0 or s[idx] != s[idx - 1]:
                    count = 1
                else:
                    count += 1
                    if count == k:
                        s = s[:idx - k + 1] + s[idx+k:]
                idx += 1
        return s


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = [0] * len(s)
        idx = 0
        while idx < len(s):
            if idx == 0 or s[idx] != s[idx - 1]:
                count[idx] = 1
            else:
                count[idx] = count[idx - 1] + 1
                if count[idx] == k:
                    s = s[:idx - k + 1] + s[idx+1:]
                    idx = idx - k
            idx += 1
        return s


class Pair:
    def __init__(self, count: int, char: str):
        self.count = count
        self.char = char


class SolutionStack:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        idx = 0
        while idx < len(s):
            if len(stack) == 0 or s[idx] != stack[-1].char:
                stack.append(Pair(1, s[idx]))
            else:
                if stack[-1].count + 1 == k:
                    stack.pop()
                else:
                    stack[-1].count += 1
            idx += 1
        result = ""
        while stack:
            pair = stack.pop(0)
            for i in range(pair.count):
                result += pair.char
        return result


if __name__ == '__main__':
    result = Solution().removeDuplicates("deeedbbcccbdaa", 3)
    print(result)

    result = Solution().removeDuplicates("pbbcggttciiippooaais", 2)
    print(result)