class Animal:
    def move(self):
        print("животное двигается")


class Swimming(Animal):
    def move(self):
        print("плавает")


class Flying(Animal):
    def move(self):
        print("летает")


class Duck(Swimming, Flying):
    def move(self):
        print("плавает и летает")

duck = Duck()
duck.move()
print(Duck.__mro__) # method resolution order