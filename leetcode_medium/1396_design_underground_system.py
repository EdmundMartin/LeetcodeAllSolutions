from collections import defaultdict


class Customer:
    def __init__(self, start_station, start_time):
        self.start_station = start_station
        self.start_time = start_time


class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.average_time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        customer = Customer(stationName, t)
        self.customers[id] = customer

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        customer = self.customers[id]
        key = f"{customer.start_station}_{stationName}"
        self.average_time[key].append(t - customer.start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        values = self.average_time[f"{startStation}_{endStation}"]
        return sum(values) / len(values)