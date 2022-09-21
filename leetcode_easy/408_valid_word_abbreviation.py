from typing import List, Tuple


def calculate_len(s: str) -> Tuple[int, List, bool]:
    count = 0
    idx = 0
    result = []
    while idx < len(s):
        if s[idx].isalpha():
            result.append(s[idx])
            idx += 1
            count += 1
        if idx < len(s) and s[idx].isdigit():
            number = ""
            while idx < len(s) and s[idx].isdigit():
                number += s[idx]
                idx += 1
            if number[0] == "0":
                return count, result, False
            result.append(int(number))
            count += int(number)
    return count, result, True


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        count, tool, valid = calculate_len(abbr)
        if not valid:
            return False
        if len(word) != count:
            return False
        idx = 0
        for ch in tool:
            if type(ch) == str:
                if word[idx] != ch:
                    return False
                idx += 1
            if type(ch) == int:
                idx += ch
        return True


if __name__ == '__main__':
    result = Solution().validWordAbbreviation("internationalization", "i12iz4n")
    print(result)

    result = Solution().validWordAbbreviation("apple", "a2e")
    print(result)

    result = Solution().validWordAbbreviation("substitution", "s10n")
    assert result is True

    result = Solution().validWordAbbreviation("substitution", "sub4u4")
    assert result is True

    result = Solution().validWordAbbreviation("substitution", "12")
    assert result is True

    result = Solution().validWordAbbreviation("substitution", "su3i1u2on")
    assert result is True
