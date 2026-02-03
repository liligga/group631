# родительский класс, суперкласс
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"car {self.model} is driving to {destination}")

# дочерний класс, подкласс, субкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"bus {self.model} is driving to {destination}")

class Truck(Car):
    pass


car_subaru = Car('silver', 'Subaru Forester')
print(car_subaru.model)
car_subaru.drive_to("Bishkek")
bus_42 = Bus("green", "MAN", 42)
print(bus_42.model)
# bus_42.drive_to("Bishkek")
print(type(bus_42))
print(isinstance(bus_42, Car))

cars = [car_subaru, bus_42]
for car in cars:
    car.drive_to("Karakol")


