from string import ascii_lowercase, ascii_uppercase, digits


conditions = [
    lambda x: len(x) >= 8,
    lambda x: any(y in ascii_lowercase for y in x),
    lambda x: any(y in ascii_uppercase for y in x),
    lambda x: any(y in digits for y in x),
    lambda x: any(y in "!@#$%^&*()-+" for y in x)
]


def check_adj_chars(pwd: str) -> bool:
    idx = 1
    while idx < len(pwd):
        if pwd[idx] == pwd[idx - 1]:
            return False
        idx += 1
    return True


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        meets_char_requirements = all(c(password) for c in conditions)
        return meets_char_requirements and check_adj_chars(password)


if __name__ == '__main__':
    test_pass = "IloveLe3tcode!"
    result = Solution().strongPasswordCheckerII(test_pass)
    print(result)
