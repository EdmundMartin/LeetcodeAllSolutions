

def largest_number(s: str, dir: str):
    largest = 0
    while s:
        int_repr = int(s)
        if int_repr % 2 != 0 and int_repr > largest:
            largest = int_repr
        if dir == "R":
            s = s[1:]
        else:
            s = s[:-1]
    return largest


class SolutionToSlow:
    def largestOddNumber(self, num: str) -> str:
        maximum = max(largest_number(num, "R"), largest_number(num, "L"))
        if maximum == 0:
            return ""
        return str(maximum)


class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num) - 1
        while idx >= 0:
            if int(num[idx]) % 2 == 1:
                return num[:idx + 1]
            idx -= 1
        return ""