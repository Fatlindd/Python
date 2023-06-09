from cow import *

class Robot:
    """ Represents Robot """

robot1 = Robot()
robot1.name = 'Nick'
robot1.pet = cow1

print_cow(robot1.pet)

def print_cow_robot(robot1):
    print(f'name: {robot1.name}, pet\'s name: {robot1.pet.name}')
    print(f'{robot1.name}\'s pet is {robot1.pet.age} years old.')

print_cow_robot(robot1)


robot3 = Robot()
robot3.name = 'Lara'
robot3.pet = create_cow('Gummy Bear', 5)
print_cow_robot(robot3)