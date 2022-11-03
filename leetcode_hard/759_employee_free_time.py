
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)


class SolutionToSlow:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flattened = [item for sublist in schedule for item in sublist]
        start_time = min([i.start for i in flattened])
        end_time = max([i.end for i in flattened])

        timespan = end_time - start_time
        workers = [0] * (timespan + 1)

        for worker in flattened:
            for i in range(worker.start, worker.end):
                workers[i - start_time] += 1

        result = []
        i = 0
        while i < len(workers) - 1:
            if workers[i] == 0:
                tmp_i = i + 1
                while tmp_i < len(workers) - 1 and workers[tmp_i] == 0:
                    tmp_i += 1
                result.append(Interval(
                    i + start_time,
                    tmp_i + start_time,
                )
                )
                i = tmp_i
            else:
                i += 1
        return result


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        arrivals = []
        departures = []

        for intervals in schedule:
            for interval in intervals:
                arrivals.append(interval.start)
                departures.append(interval.end)

        arrivals.sort()
        departures.sort()

        n = len(arrivals)
        i, j, num, free = 0, 0, 0, []
        start = None
        while i < n and j < n:
            if arrivals[i] <= departures[j]:
                num += 1
                if num == 1 and start:
                    free.append(Interval(start, arrivals[i]))
                    start = None
                i += 1
            else:
                num -= 1
                if num == 0 and not start:
                    start = departures[j]
                j += 1
        return free


if __name__ == '__main__':
    schedule = [
        [Interval(1, 2),
        Interval(5, 6),
         ],
        [Interval(1, 3)],
        [Interval(4, 10)],
    ]

    res = Solution().employeeFreeTime(schedule)
    print(res)