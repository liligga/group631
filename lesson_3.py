class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
        self.__max_speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} is driving to {destination}, max speed: {self.__max_speed}")
        self.__test()

    def __test(self):
        self.__max_speed = 20
        print(f"Car {self.model} is {self._fined}")

    # геттер - получаем
    def get_max_speed(self):
        return self.__max_speed

    # сеттер - устанавливаем
    def set_max_speed(self, value):
        self.__max_speed = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        print(f"внутри сеттера {value}")
        if value <= 0:
            raise ValueError("Максимальная скорость не может быть меньше 0")
        self.__max_speed = value

car_subaru = Car('silver', 'Subaru Forester')
print(car_subaru.model)
car_subaru.drive_to("Karakol")
print(car_subaru._fined)
car_subaru._fined = True
# car_subaru.__test()
# print(car_subaru.__max_speed)
# car_subaru.max_speed = 150   - не правильно
print(car_subaru._Car__max_speed)  # это только во время разработки
print("Max speed", car_subaru.get_max_speed())
car_subaru.set_max_speed(100)
print("New max speed", car_subaru.get_max_speed())

print(car_subaru.max_speed)
car_subaru.max_speed = -200
print(car_subaru.max_speed)
