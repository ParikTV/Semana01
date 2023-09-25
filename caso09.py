class Persona:
    """The __init__() function is called automatically every time the
    class is being used to create a new object."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    """ The self parameter is a reference to the current 
    instance of the class, and is used to access variables
    that belong to the class."""

    """the @property decorator lets us make a method behave like an attribute"""

    @property
    def mostrar(self):
        mensa = "Mi nombre es {} y Yo tengo {} años de edad.".format(self.nombre, self.edad)
        return mensa
        # "%s %s" % (self.nombre, str(self.edad)))


if __name__ == '__main__':
    person = Persona("Huberth", 43)
    print(person.mostrar)  # no brackets
