

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        value = self.spaces[carType]
        can_park = value > 0
        self.spaces[carType] -= 1
        return can_park
