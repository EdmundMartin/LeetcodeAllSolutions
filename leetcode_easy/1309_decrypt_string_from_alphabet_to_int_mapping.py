from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = {}
        for idx, ch in enumerate(ascii_lowercase):
            res[idx + 1] = ch
        idx = 0
        result = ""
        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == "#":
                key = int(''.join(s[idx:idx+2]))
                result += res[key]
                idx += 3
            else:
                key = int(s[idx])
                result += res[key]
                idx += 1
        return result


if __name__ == '__main__':
    test_val = "10#11#12"
    res = Solution().freqAlphabets(test_val)
    print(res)