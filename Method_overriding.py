class Employee :
    def working_hours(self):
        return 45

class Intern(Employee) :
    def working_hours(self):
        return 50


i1=Intern()
print(i1.working_hours())