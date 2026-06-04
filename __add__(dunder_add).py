class Rectangle:
    def __init__(self,length,breadth,):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def __add__(self,other):
        return  Rectangle (self.length+other.length,self.breadth+other.breadth)

r1=Rectangle(3,4)
r2=Rectangle(5,6)
print(r1.area())
print(r2.area())
r3= r1+r2
print(r3.area())