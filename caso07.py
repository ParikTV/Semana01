import datetime  # we will use this for date objects


class Persona:
    """The __init__() function is called automatically every time the
    class is being used to create a new object."""

    def __init__(self, nombre, edad, cumpleanhos):
        self.nombre = nombre
        self.edad = edad
        self.cumpleanhos = cumpleanhos

    def mostraredad(self):
        today = datetime.date.today()
        age = today.year - self.cumpleanhos.year

        if today < datetime.date(today.year, self.cumpleanhos.month, self.cumpleanhos.day):
            age -= 1

        return age

    """ The self parameter is a reference to the current 
    instance of the class, and is used to access variables
    that belong to the class."""

    def mostrar(self):
        print("Me presento mi nombre es: " + self.nombre + " y actualmente mi edad es: " + str(self.edad))


if __name__ == '__main__':
    person = Persona("Hubert", 43, datetime.date(1979, 12, 2))  # year, month, day
    print(person.nombre)
    print(person.edad)
    print(person.mostrar())
    print(person.mostraredad())
