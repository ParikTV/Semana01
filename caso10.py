from caso02 import Persona


class Docente(Persona):
    pass


if __name__ == '__main__':
    docen = Docente("Huberth", 43)
    print(docen.nombre)
    print(docen.edad)
