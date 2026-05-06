"""
Property or behaviour derived(inherited) from parents(base class) (Parent -> child ) # is a Relationship
"""
class Vehicle :
    company ="XYZ company"

    def __init__(self ,wheels ,seats,milage):
        self.wheels = wheels
        self.seats = seats
        self.milage = milage

    def get_details(self):
        return f"Vehicle is of {self.company} company \nhas {self.wheels} wheels {self.seats} seats and provides milage of  {self.milage}"


# s1=Vehicle(4,4,30)
# print(s1.get_details())


class Car (Vehicle):
    pass
#Car class inherits the Vehicle class
#Car class is called the child class or derived class
#vehicle class is called parent class or base class
c1=Car( 4,4,30)
print(c1.get_details())
