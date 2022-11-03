from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        size = len(temperatures)
        hottest = 0
        answer = [0] * size

        idx = size - 1
        while idx >= 0:
            current_temperature = temperatures[idx]

            if current_temperature >= hottest:
                hottest = current_temperature
                idx -= 1
                continue

            days = 1
            while temperatures[idx + days] <= current_temperature:
                days += answer[idx + days]
            answer[idx] = days
            idx -= 1
        return answer
