"""
Method overloading is an Object-Oriented Programming concept
where a class can have multiple methods with the same name
but different parameters. It allows a method to perform different
operations based on the number or type of arguments passed.

However, Python does not support true method overloading.
Instead, it achieves similar behavior using *args (variable-length arguments).
"""

class Calculator:
    def add(self, *args):
        return sum(args)

# Creating object
calc = Calculator()

# Calling method with different number of arguments
print(calc.add(1, 2))          # Output: 3
print(calc.add(1, 2, 3))       # Output: 6
print(calc.add(10, 20, 30, 40))# Output: 100