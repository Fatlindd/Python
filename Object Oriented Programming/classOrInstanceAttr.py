class Person:
    # Define the class parameter 'name'
    name = 'Person'

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name

fatlind = Person('Fatlind')
print("%s name is %s" % (Person.name, fatlind.name))

erblina = Person()
erblina.name = 'Erblina'
print("%s name is %s" % (Person.name, erblina.name))