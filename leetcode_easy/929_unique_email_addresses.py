from typing import List


def normalize_part(s: str, domain_part: bool):
    if not domain_part:
        s = s.replace(".", '')
    return s.split('+')[0]


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            parts = email.split("@")
            cleaned = normalize_part(parts[0], False) + "@" + normalize_part(parts[1], True)
            unique.add(cleaned)
        return len(unique)


if __name__ == '__main__':
    examples = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    res = Solution().numUniqueEmails(examples)
    print(res)