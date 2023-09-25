from caso02 import Persona


class Docente(Persona):
    """Python also has a super() function that will make the child class
    inherit all the methods and properties from its parent"""

    def __init__(self, nombre, edad, especialidad, gradoacademico, clase):
        super().__init__(nombre, edad)
        self.titulo = especialidad
        self.grado = gradoacademico
        self.clase = clase

    def asignacion(self):
        print("Bienvenido Profesor", self.nombre, "a la clase de ", self.clase)


if __name__ == '__main__':
    docen = Docente("Huberth", 43, "Informático", "MSC", "Programación II")
    print(docen.nombre + " " + str(docen.edad) + " " + docen.titulo + " " + docen.grado)
    print("\n")
    docen.asignacion()
