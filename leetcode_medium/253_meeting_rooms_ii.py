from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if len(intervals) == 0:
            return 0

        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]

        start.sort()
        end.sort()

        start_pointer = 0
        end_pointer = 0

        used_rooms = 0

        while start_pointer < len(intervals):

            if start[start_pointer] >= end[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms
