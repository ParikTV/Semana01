class Persona:

    Titulos = ('Dr', 'Mr', 'Mrs', 'Ms')

    """The __init__() function is called automatically every time the
    class is being used to create a new object."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    """ We can call them from an instance or a class object, 
    but they are most commonly called from class objects, like class methods."""
    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        # class or instance object accessible through cls
        return [t for t in cls.Titulos if t.startswith(startswith)]

    """A static method doesn’t have the calling object passed into it as the first parameter. 
    This means that it doesn’t have access to the rest of the class or instance at all."""
    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
        # no parameter for class or instance object
        # we have to use Person directly
        return [t for t in Persona.Titulos if t.endswith(endswith)]


if __name__ == '__main__':
    person = Persona("Hubert", 43)
    print(person.allowed_titles_starting_with("M"))
    print(Persona.allowed_titles_starting_with("M"))

    print(person.allowed_titles_ending_with("s"))
    print(Persona.allowed_titles_ending_with("s"))
