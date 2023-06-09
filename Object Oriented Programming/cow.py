class Cow:
    """ Represents a cow """

cow1 = Cow()

#1 
cow1.name = 'Rose'
cow1.age = 3

def print_cow(cow1):
    print(f'name: {cow1.name}, age: {cow1.age}')

# print_cow(cow1)

def create_cow(name, age):
    cow = Cow()
    cow.name, cow.age = name, age
    return cow

