class Administrativo:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.materias = {}

    def asignar_docente(self, materia, docente):
        self.materias[materia] = docente
        print(f"El docente {docente} fue asignado a la materia {materia}")

    def mostrar_asignaciones(self):
        print(f"\nAsignaciones de {self.nombre}:")
        for materia, docente in self.materias.items():
            print(f"- {materia}: {docente}")


class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []
        self.administrativos = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def agregar_administrativo(self, administrativo):
        self.administrativos.append(administrativo)

    def mostrar_materias(self):
        print(f"\nMaterias de la carrera {self.nombre}:")
        for materia in self.materias:
            print(f"- {materia}")

    def mostrar_administrativos(self):
        print(f"\nPersonal administrativo de {self.nombre}:")
        for administrativo in self.administrativos:
            print(f"- {administrativo.nombre}")
