class Vehicle :
    company ="XYZ company"

    def __init__(self ,wheels ,seats,milage):
        print("init Vehicle")
        self.wheels = wheels
        self.seats = seats
        self.milage = milage

    def get_details(self):
        return f"Vehicle is of {self.company} company \nhas {self.wheels} wheels {self.seats} seats and provides milage of  {self.milage}"

class Car (Vehicle):
    model="ABC123"
    def __init__(self ,car_type,drive_type,wheels,seats,milage):#drive_type is auto or manual
        super().__init__(wheels,seats,milage) #also can use Vehicle.__init__ just need to pass self also
        print("init Car")
        self.car_type = car_type
        self.drive_type = drive_type

    def display_details(self):
        print(f"car type is {self.car_type}")
        print(f"drive type is {self.drive_type}")
        print(f"wheels is {self.wheels}")
        print(f"seats is {self.seats}")

class ElectricCar(Car):
    def __init__(self,car_type,drive_type,wheels,seats,milage,battery,distance):
        print("init E_vehicle")

        self.battery=battery
        self.distance = distance
        super().__init__(car_type,drive_type,wheels,seats,milage)

    def change_battery(self):
        print(f"change battery to {self.battery}")

c1=ElectricCar("suv","Manual",4,5,30,100,300)
print(c1.__dict__)
help(ElectricCar)