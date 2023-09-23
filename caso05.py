class Persona:
    """Python classes have a special method called.__new__(),
    which is responsible
    for creating and returning a new empty object."""

    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Persona.")
        return super().__new__(cls)

    """Then another special method,.__init(), takes the resulting object,
    along with the class constructors arguments. The method also takes
    *args and **kwargs,
    which allow for passing an undefined number of initialization
    arguments to the underlying instance."""

    def __init__(self, nombre, edad):
        print("2. Initialize the new instance of Persona.")
        self.x = nombre
        self.y = edad

    """._repr_() special method, which provides a proper string
    representation for your Persona class."""

    def __repr__(self) -> str:
        return f"{type(self).__name__}x={self.x}, y={self.y})"


if __name__ == '__main__':
    person = Persona("Justin", 20)
    print(person.x)
    print(person)
    print(person.y)
    print(person.__repr__())
