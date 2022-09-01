from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if len(stack) > 0:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)


if __name__ == '__main__':
    logs = ["d1/","d2/","../","d21/","./"]
    result = Solution().minOperations(logs)
    print(result)

    logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
    result = Solution().minOperations(logs)
    print(result)

    logs = ["d1/","../","../","../"]
    result = Solution().minOperations(logs)
    print(result)