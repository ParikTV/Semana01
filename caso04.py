class Persona:
    """The__init__() function is called automatically every time
    the class is being used to create a new object"""
    def __init__(mipalabra, nombre, edad):
        mipalabra.nombre = nombre
        mipalabra.edad = edad

    """The self parameter is a reference to the current
    instance of the class, and is used to access variables
    that belong to the class """
    def mostrar(mipalabra):
        print("Me presento mi nombre es: " + mipalabra.nombre +
            ' y actualmente mi edad es: ' + str(mipalabra.edad))



if __name__ == '__main__':
            person = Persona("Justin", 20)
            print(person.nombre)
            print(person.edad)
