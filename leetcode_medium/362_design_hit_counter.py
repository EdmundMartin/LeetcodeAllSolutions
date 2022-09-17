import heapq


class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.hits, timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.hits) > 0 and timestamp - self.hits[0] >= 300:
            heapq.heappop(self.hits)
        return len(self.hits)


if __name__ == '__main__':
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    res = counter.getHits(4)
    print(res)
    counter.hit(300)
    res = counter.getHits(300)
    print(res)
    res = counter.getHits(301)
    print(res)