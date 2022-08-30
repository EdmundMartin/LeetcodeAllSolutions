

class Solution:
    def checkRecord(self, s: str) -> bool:
        absence = 0
        late_count = 0
        for ch in s:
            if ch == 'A':
                absence += 1
                late_count = 0
            elif ch == 'L':
                late_count += 1
                if late_count == 3:
                    return False
            else:
                late_count = 0
        return absence < 2


if __name__ == '__main__':
    result = Solution().checkRecord("PPALLP")
    assert result is True

    result = Solution().checkRecord("PPALLL")
    assert result is False
