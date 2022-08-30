

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = float('-inf')
        prev = None
        count = 0
        for ch in num:
            if prev is None:
                prev = ch
                count = 1
            else:
                if ch == prev:
                    count += 1
                else:
                    prev = ch
                    count = 1
            if count == 3:
                if int(ch) > largest:
                    largest = int(ch)
        if largest == float('-inf'):
            return ""
        return str(largest) * 3


if __name__ == '__main__':
    test_val = "6777133339"
    res = Solution().largestGoodInteger(test_val)
    print(res)