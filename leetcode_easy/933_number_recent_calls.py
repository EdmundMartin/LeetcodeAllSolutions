import heapq


class RecentCounter:

    def __init__(self):
        self.heap = []

    def ping(self, t: int) -> int:
        heapq.heappush(self.heap, t)
        while self.heap and self.heap[0] < t - 3000:
            heapq.heappop(self.heap)
        return len(self.heap)