class ParkingSystem:
    b = 0
    m = 0
    s = 0

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small
        
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.b > 0:
                self.b -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.m > 0:
                self.m -= 1
                return True
            else:
                return False
        else:
            if self.s > 0:
                self.s -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)