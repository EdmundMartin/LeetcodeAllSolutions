

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(string: s, open_symbol, close_symbol):
            result = []
            balance = 0
            for char in string:
                if char == open_symbol:
                    balance += 1
                if char == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                result.append(char)
            return "".join(result)

        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]


if __name__ == '__main__':
    Solution().minRemoveToMakeValid("lee(t(c)o)de)")