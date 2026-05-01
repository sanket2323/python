class Car:

    wheel_diameter = 6 #this is in inch
    num_car = 0
    def __init__(self, model,year,for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale
        # self.num_car += 1  # it will not increament
        Car.num_car += 1



    def car_drive(self):
        print(f"You can drive the car {self.model}")

    def car_stop(self):
        print("You can stop the car")