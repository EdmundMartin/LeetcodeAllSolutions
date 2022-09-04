from typing import List
from collections import defaultdict


def variants(domain: str):
    all_vars = []
    while "." in domain:
        all_vars.append(domain)
        parts = domain.split('.')
        parts = parts[1:]
        domain = '.'.join(parts)
    all_vars.append(domain)
    return all_vars


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)

        for domain in cpdomains:
            count, tmp_domain = domain.split(' ')
            for var in variants(tmp_domain):
                counter[var] += int(count)
        return [
            "{} {}".format(v, k) for k, v in counter.items()
        ]


if __name__ == '__main__':
    result = Solution().subdomainVisits(["9001 discuss.leetcode.com"])
    print(result)

    result = Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(result)