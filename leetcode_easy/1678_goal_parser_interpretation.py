

class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        idx = 0
        while idx < len(command):
            ch = command[idx]
            if ch == "G":
                result += ch
                idx += 1
            elif ch == "(":
                if command[idx+1] == ")":
                    result += "o"
                    idx += 2
                else:
                    result += "al"
                    idx += 4
        return result


if __name__ == '__main__':
    test_data = "G()()()()(al)"
    res = Solution().interpret(test_data)
    print(res)

    test_data_two = "(al)G(al)()()G"
    res = Solution().interpret(test_data_two)
    print(res)