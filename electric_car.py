from car import Car

class Battery():
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()