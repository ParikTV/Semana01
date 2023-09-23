class Persona:
    """The__init__() function is called automatically every time
    the class is being used to create a new object"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    """The self parameter is a reference to the current
    instance of the class, and is used to access variables
    that belong to the class """
    def mostrar(self):
        print("Me presento mi nombre es: " + self.nombre +
              ' y actualmente mi edad es: ' + str(self.edad))


if __name__ == '__main__':
    person = Persona("Justin", 20)
    print(person.nombre)
    print(person.edad)
    print(person.mostrar())
