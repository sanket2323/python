# class: Blue print for creating something
# object: object created from the blue print
# method: functions inside the class
from car import Car
car1 = Car("Mercedes","2009",False)
car2 = Car("Mercedes","2019",True)
print(car1.model)
print(Car.wheel_diameter)
print(Car.num_car)
car2.car_drive()