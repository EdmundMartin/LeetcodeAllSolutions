

def build_idx_mapping(s: str):
    mapping = {}
    for idx, ch in enumerate(s):
        mapping[idx] = ch
    return mapping


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        if sorted_s1 != sorted_s2:
            return False
        first, second = build_idx_mapping(s1), build_idx_mapping(s2)
        count = 0
        for idx in range(len(s1)):
            if first[idx] != second[idx]:
                count += 1
        return count <= 2


if __name__ == '__main__':
    result = Solution().areAlmostEqual("abcd", "dcba")
    print(result)