from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for elevate in gain:
            altitude += elevate
            max_altitude = max(max_altitude, altitude)
        return max_altitude
