from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        results = []
        for ch in ops:
            if ch == "C":
                results = results[:-1]
            elif ch == "D":
                to_add = results[-1] * 2
                results.append(to_add)
            elif ch == "+":
                results.append(results[-1] + results[-2])
            else:
                results.append(int(ch))
        return sum(results)


if __name__ == '__main__':
    res = Solution().calPoints(["5","2","C","D","+"])
    print(res)

    res = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
    print(res)

    res = Solution().calPoints(["1", "C"])
    print(res)