from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав гав")

    def test(self):
        print("test in Dog")

    def testest(self):
        print("test test in Dog")

class Cat(Animal):
    pass


puppy = Dog()
puppy.make_sound()