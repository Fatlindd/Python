# Python eshte mënyra per te shmangur metodat getter dhe setter ne kodin
# tuaj. Ky funksioni na lejon te kthejm atributet e klasës ne property(veti) ose ne atribute te
# menaxhuara.

# property(fget=None, fset=None, fdel=None, doc=None)
# Properties janë atribute te klasës qe menaxhojnë atributet e instancës.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )


circle = Circle(42.0)
print(circle.radius)

circle.radius = 10
print(circle.radius)



############### Decorator ###############
"""
@decorator
def func(a):
    return a

def func(a):
    return a

func = decorator(func)
"""


"""
class Circle:
    def __init__(self, radius):
    self._radius = radius
    
    @property
    def radius(self):
        # The radius property.
        print("Get radius.")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value
"""