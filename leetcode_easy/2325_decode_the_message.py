from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        idx = 0
        mapping = {}
        for char in key:
            if idx == len(ascii_lowercase):
                break
            if char == " ":
                continue
            if char in mapping:
                continue
            mapping[char] = ascii_lowercase[idx]
            idx += 1
        result = ""
        for char in message:
            if char == " ":
                result += " "
                continue
            result += mapping[char]
        return result


if __name__ == '__main__':
    test_key = "the quick brown fox jumps over the lazy dog"
    test_msg = "vkbs bs t suepuv"

    result = Solution().decodeMessage(test_key, test_msg)
    print(result)