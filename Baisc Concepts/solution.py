
#self is used as context 

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def full_name(self):
        print(f"{self.brand} {self.color}")


class ElectricCar(Car):
    def __init__(self, brand, color,batter_size):
        super().__init__(brand, color)
        self.batter_size = batter_size

    

my_car = Car("sanket","black")
print(my_car.brand)