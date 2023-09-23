class Persona:
    """The__init__() function is called automatically every time
    the class is being used to create a new object"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


if __name__ == '__main__':
    person = Persona("Justin", 20)
    print(person.nombre)
    print(person.edad)
