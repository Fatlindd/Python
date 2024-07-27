"""
    namedTuple is a function for creating tuple subclasses with named fields. namedTuple provides
    a way to create lightweight, immutable data structures that are more readable and self-documenting than
    regular tuples.
"""

# ------------------------------------------------------------------------------------------------------------
# Basic Example
from collections import namedtuple

# Define a namedTuple called 'Point'
Point = namedtuple('Points', ['x', 'y'])

# Create an instance of Point
p = Point(11, 22)
# print(p)           # Output: Point(x=11, y=22)
# print(p.x, p.y)    # Output: 11 22

# ------------------------------------------------------------------------------------------------------------

# Exercise 1: Representing a Coordinate Point
# Define the namedTuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances of Point
point1 = Point(10, 20)
point2 = Point(30, 40)

# Access coordinates
# print(f"Point1: x={point1.x}, y={point1.y}")  # Output: Point1: x=10, y=20
# print(f"Point2: x={point2[0]}, y={point2[1]}")  # Output: Point2: x=30, y=40

# ------------------------------------------------------------------------------------------------------------

# Exercise 2: Storing Employee Data
Employee = namedtuple('Employee', ['name', 'age', 'department'])

# Create instances of Employee
emp1 = Employee('Alice', 30, 'HR')
emp2 = Employee('Bob', 24, 'Engineering')

# Display employee details
# print(f"Employee1: Name={emp1.name}, Age={emp1.age}, Department={emp1.department}")
# print(f"Employee2: Name={emp2[0]}, Age={emp2[1]}, Department={emp2[2]}")

# Output:
# Employee1: Name=Alice, Age=30, Department=HR
# Employee2: Name=Bob, Age=24, Department=Engineering

# ------------------------------------------------------------------------------------------------------------

# Exercise 3: Representing a Car
Car = namedtuple('Car', ['make', 'model', 'year', 'color'])

# Create instances of Car
car1 = Car('Toyota', 'Camry', 2020, 'Blue')
car2 = Car('Honda', 'Civic', 2018, 'Red')

# Display car attributes
print(f"Car1: Make={car1.make}, Model={car1.model}, Year={car1.year}, Color={car1.color}")
print(f"Car2: Make={car2[0]}, Model={car2[1]}, Year={car2[2]}, Color={car2[3]}")

# Output:
# Car1: Make=Toyota, Model=Camry, Year=2020, Color=Blue
# Car2: Make=Honda, Model=Civic, Year=2018, Color=Red

# ------------------------------------------------------------------------------------------------------------

# When to Use namedtuple
"""
----------------------------------------------------------------------------------------------------------------

1. Readability and Self-Documentation: When you want to make your code more readable and self-documenting by giving 
meaningful names to the fields of your tuples. This can help other developers understand the purpose of each element 
without needing additional comments or documentation.
from collections import namedtuple

# Example: Representing a coordinate point
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x, point.y)  # Output: 10 20

----------------------------------------------------------------------------------------------------------------

1. Readability and Self-Documentation: When you want to make your code more readable and self-documenting by giving 
meaningful names to the fields of your tuples. This can help other developers understand the purpose of each element 
without needing additional comments or documentation.
from collections import namedtuple

# Example: Representing a coordinate point
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x, point.y)  # Output: 10 20

----------------------------------------------------------------------------------------------------------------
2. Immutability: When you need a lightweight, immutable data structure. namedtuple instances are immutable, which means
 their values cannot be changed after they are created. This is useful when you want to ensure that your data remains 
 constant throughout the program.

# Example: Representing a car
Car = namedtuple('Car', ['make', 'model', 'year', 'color'])
car = Car('Toyota', 'Camry', 2020, 'Blue')
# car.year = 2021  # This would raise an AttributeError

----------------------------------------------------------------------------------------------------------------

2. Immutability: When you need a lightweight, immutable data structure. namedtuple instances are immutable, which means
 their values cannot be changed after they are created. This is useful when you want to ensure that your data remains 
 constant throughout the program.

# Example: Representing a car
Car = namedtuple('Car', ['make', 'model', 'year', 'color'])
car = Car('Toyota', 'Camry', 2020, 'Blue')
# car.year = 2021  # This would raise an AttributeError

----------------------------------------------------------------------------------------------------------------

3. Memory Efficiency: When you need a memory-efficient data structure. namedtuple instances use less memory than 
regular classes because they do not have a __dict__ attribute to store instance variables.

# Example: Representing an employee
Employee = namedtuple('Employee', ['name', 'age', 'department'])
emp = Employee('Alice', 30, 'HR')

----------------------------------------------------------------------------------------------------------------

4. Replacing Dictionaries: When you are using dictionaries to represent simple data structures and want to avoid the 
overhead and complexity of dictionaries. namedtuple can provide a more structured and cleaner alternative.

# Example: Replacing a dictionary
# Instead of using a dictionary
employee_dict = {'name': 'Alice', 'age': 30, 'department': 'HR'}
print(employee_dict['name'])  # Output: Alice

# Use namedtuple
Employee = namedtuple('Employee', ['name', 'age', 'department'])
emp = Employee('Alice', 30, 'HR')
print(emp.name)  # Output: Alice

----------------------------------------------------------------------------------------------------------------

5. Return Multiple Values: When you want to return multiple values from a function with meaningful names. This can make 
your function returns more intuitive and easier to use.

# Example: Returning multiple values from a function
def get_car_info():
    Car = namedtuple('Car', ['make', 'model', 'year'])
    return Car('Toyota', 'Camry', 2020)

car = get_car_info()
print(car.make, car.model, car.year)  # Output: Toyota Camry 2020

----------------------------------------------------------------------------------------------------------------
"""