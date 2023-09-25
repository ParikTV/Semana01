class Persona:
    """Python classes have a special method called.__new__(), which is responsible
    for creating and returning a new empty object."""

    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Persona.")
        return super().__new__(cls)

    """Then another special method,.__init__(), takes the resulting object, along
    with the class constructor’s arguments. The method also takes *args and **kwargs, 
    which allow for passing an undefined number of initialization
     arguments to the underlying instance."""

    def __init__(self, nombre, edad):
        print("2. Initialize the new instance of Persona.")
        self.x = nombre
        self.y = edad

    """ .__repr__() special method, which provides a proper string representation for your Persona class."""

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def mostrar(self):
        print("Me presento mi nombre es: " + self.x + " y actualmente mi edad es: " + str(self.y))

    """ First place the @classmethod decorator above the method definition. For now, you just need to understand 
    that the @classmethod decorator will change an instance method to a class method."""

    """The create_anonymous() method cannot access instance attributes.But it can
    access class attributes via the cls variable."""

    @classmethod
    def create_anonymous(cls):
        return Persona('Keitlyn', 11)


if __name__ == '__main__':
    person = Persona("Hubert", 43)
    anonymous = person.create_anonymous()
    print(person.x)
    print(person.y)
    print(person.__repr__())
    print(anonymous.mostrar())
