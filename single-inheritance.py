
class Vehicle :
    company ="XYZ company"

    def __init__(self ,wheels ,seats,milage):
        print("init Vehicle")
        self.wheels = wheels
        self.seats = seats
        self.milage = milage

    def get_details(self):
        return f"Vehicle is of {self.company} company \nhas {self.wheels} wheels {self.seats} seats and provides milage of  {self.milage}"


# s1=Vehicle(4,4,30)
# print(s1.get_details())


class Car (Vehicle):
    model="ABC123"
    def __init__(self ,car_type,drive_type):#drive_type is auto or manual
        super().__init__(4,4,30) #also can use Vehicle.__init__ just need to pass self also
        print("init Car")
        self.car_type = car_type
        self.drive_type = drive_type

c1=Car("suv","aauto")
print(c1.company)
print(c1.model)
print(c1.milage)
print(c1.get_details())
print(c1.__dict__)