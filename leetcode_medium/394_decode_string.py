


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_str = ''

        for char in s:
            if char == '[':
                stack.append(current_str)
                stack.append(current_number)
                current_str = ''
                current_number = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_str = prev_string + (num * current_str)
            elif char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                current_str += char
        return current_str


if __name__ == '__main__':
    input_example = "3[a]2[bc]"
    res = Solution().decodeString(input_example)
    print(res)