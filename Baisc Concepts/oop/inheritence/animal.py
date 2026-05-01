class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def is_eating(self):
        print(f"{self.name} is eating")

    def is_sleeping(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):
    pass
class Dog(Animal):
    pass

cat1 = Cat("Manu")
print(cat1.is_eating())