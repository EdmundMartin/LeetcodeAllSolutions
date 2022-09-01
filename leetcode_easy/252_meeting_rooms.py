from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        idx = 0
        while idx < len(intervals) - 1:
            if intervals[idx][1] > intervals[idx + 1][0]:
                return False
            idx += 1
        return True
